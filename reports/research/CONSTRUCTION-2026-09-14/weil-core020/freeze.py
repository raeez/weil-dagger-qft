from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess

R = Path(__file__).resolve().parent
W = R.parents[3]
S = W / 'research-candidates/weil-core020'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(name, value):
    (R / name).write_text(json.dumps(value, indent=2) + '\n')

sources = sorted(p for p in S.rglob('*') if p.is_file())
assert len(sources) == 26
patches = []
for p in sources:
    result = subprocess.run(['git', 'diff', '--no-index', '--binary', '--', '/dev/null', str(p.relative_to(W))],
                            cwd=W, capture_output=True)
    assert result.returncode == 1, (p, result.returncode, result.stderr)
    patches.append(result.stdout)
patch = R / 'reader-source-additions.patch'
patch.write_bytes(b''.join(patches))
command = ['git', 'apply', '--reverse', '--check', str(patch)]
check = subprocess.run(command, cwd=W, capture_output=True, text=True)
assert check.returncode == 0, check.stderr
save('patch-verification.json', {'command': command, 'returncode': check.returncode,
     'stdout': check.stdout, 'stderr': check.stderr, 'source_files': 26,
     'patch_sha256': sha(patch), 'scope': 'Read-only reverse applicability check against the exact current additions. No patch was applied.'})

renders = json.loads((R / 'render-map.json').read_text())
fullpages = [x['page'] for x in renders['full']['rendered']]
standpages = [x['page'] for x in renders['standalone']['rendered']]
save('visual-inspection.json', {'full_pdf_sha256': renders['full']['pdf_sha256'],
     'standalone_pdf_sha256': renders['standalone']['pdf_sha256'],
     'full_pages_inspected': fullpages, 'standalone_pages_inspected': standpages,
     'full_adjacent_pairs_inspected': [[n, n+1] for n in fullpages if n+1 in fullpages],
     'standalone_adjacent_pairs_inspected': [[n, n+1] for n in standpages if n+1 in standpages],
     'method': 'Full page raster comparisons, visual inspection of all 15 contact sheets, and an original-resolution header check on full page 323.',
     'new_layout_or_firewall_defects': [],
     'separate_inherited_navigation_defects': '53 exact baseline records in all-label-destinations.json'})
status = subprocess.check_output(['git', 'status', '--porcelain=v1', '--untracked-files=all'], cwd=W, text=True)
(R / 'git-status.txt').write_text(status)
for line in status.splitlines():
    path = line[3:]
    assert path.startswith(('research-candidates/weil-core020/', 'reports/research/CONSTRUCTION-2026-09-14/weil-core020/')), path
    assert line.startswith('?? '), line
assert not subprocess.check_output(['git', 'diff', '--cached', '--name-only'], cwd=W, text=True).strip()

excluded = {'freeze.json', 'freeze-check.json'}
paths = sorted(sources + [p for p in R.rglob('*') if p.is_file() and not (p.parent == R and p.name in excluded)])
rows = [{'path': str(p.relative_to(W)), 'sha256': sha(p), 'bytes': p.stat().st_size} for p in paths]
aggregate = hashlib.sha256(json.dumps(rows, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
manifest = {'schema': 1, 'candidate': 'weil-core020', 'created_utc': datetime.now(timezone.utc).isoformat(),
    'status': 'Frozen construction for scoped independent review. Root acceptance required. Inherited whole-book navigation defects remain.',
    'repository': str(W), 'principal_base_commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=W, text=True).strip(),
    'branch': subprocess.check_output(['git', 'branch', '--show-current'], cwd=W, text=True).strip(),
    'source_root': str(S.relative_to(W)), 'source_closure': str((R/'source-closure.json').relative_to(W)),
    'source_closure_sha256': sha(R/'source-closure.json'),
    'source_aggregate_sha256': json.loads((R/'source-closure.json').read_text())['source_aggregate_sha256'],
    'source_patch': str(patch.relative_to(W)), 'source_patch_sha256': sha(patch),
    'core_semantic_diff_sha256': sha(R/'core-semantic-integration.diff'),
    'pdfs': json.loads((R/'verification-results.json').read_text())['pdfs'],
    'proof_preservation': {'native': 33, 'native_byte_identical': 32, 'native_notation_only': 1, 'core_exact': 138, 'new_proofs': 4},
    'navigation': {'all_destinations_exist': 799, 'new_chapter_labels_correct': 127, 'inherited_baseline_discrepancies': 53, 'new_discrepancies': 0},
    'runtime_controls': {'required_model': 'gpt-6-astra', 'required_effort': 'ultra', 'observed_metadata': 'unavailable; unverified'},
    'excluded_self_referential_files': ['freeze.json', 'freeze-check.json'], 'files': rows, 'file_count': len(rows),
    'aggregate_serialization': 'UTF-8 json.dumps(files, sort_keys=True, separators=(comma,colon))',
    'aggregate_sha256': aggregate}
save('freeze.json', manifest)
for row in rows:
    assert sha(W / row['path']) == row['sha256'], row
save('freeze-check.json', {'manifest_sha256': sha(R/'freeze.json'), 'files_verified': len(rows),
     'aggregate_sha256': aggregate, 'all_files_match': True, 'source_assets_unchanged': True})
print(json.dumps({'manifest_sha256': sha(R/'freeze.json'), 'files': len(rows), 'aggregate_sha256': aggregate,
                  'source_patch_sha256': sha(patch)}))
