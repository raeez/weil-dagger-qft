from pathlib import Path
import difflib
import hashlib
import json
import re
import shutil
import subprocess
import sys
import zipfile
import fitz
from pypdf import PdfReader

R = Path(__file__).resolve().parent
W = R.parents[3]
S = W / 'research-candidates/weil-core020'
C = R / 'custody019'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
digest = lambda b: hashlib.sha256(b).hexdigest()
def save(name, value):
    (R / name).write_text(json.dumps(value, indent=2) + '\n')

custody = json.loads((R / 'custody-import.json').read_text())
for row in custody['rows']:
    assert sha(row['original']) == row['sha256'], row
    assert sha(W / row['copy']) == row['sha256'], row
prior = json.loads((C / 'inputs/03-freeze.json').read_text())
oldroot = Path('/Users/raeez/mathematics/worktrees/frontier-mine-weil-20260913')
for row in prior['files']:
    assert sha(oldroot / row['path']) == row['sha256'], row
closure = json.loads((C / 'source-closure.json').read_text())
for row in closure['files']:
    assert sha(S / row['path']) == row['sha256'], row
assert len(closure['files']) == 26
save('source-closure.json', closure)
save('custody-verification.json', {'imported_files_verified': len(custody['rows']),
     'prior_native_freeze_rows_verified': len(prior['files']),
     'all26_source_assets_unchanged': True})

native = (C / 'inputs/04-paper.tex').read_text()
chapter = (S / 'manuscript/weil-forms-and-domains.tex').read_text()
proof_pattern = r'\\begin\{proof\}.*?\\end\{proof\}'
normalize = lambda t: t.replace('_{\\rm vM}', '_{\\mathrm{vM}}')
rows = []
for number, match in enumerate(re.finditer(proof_pattern, native, re.S), 1):
    block = normalize(match.group())
    assert chapter.count(block) == 1
    start = chapter.index(block)
    rows.append({'number': number, 'old_start_line': native[:match.start()].count('\n') + 1,
                 'new_start_line': chapter[:start].count('\n') + 1,
                 'old_sha256': digest(match.group().encode()), 'new_sha256': digest(block.encode()),
                 'byte_identical': block == match.group()})
assert len(rows) == 33 and sum(r['byte_identical'] for r in rows) == 32
core, proofs, deltas = [], [], []
for path in sorted((C / 'baseline-source').rglob('*.tex')):
    rel = path.relative_to(C / 'baseline-source')
    current = S / rel
    before, after = path.read_text(), current.read_text()
    for number, match in enumerate(re.finditer(proof_pattern, before, re.S), 1):
        assert after.count(match.group()) == 1, (rel, number)
        proofs.append({'path': str(rel), 'number': number,
            'baseline_line': before[:match.start()].count('\n') + 1,
            'current_line': after[:after.index(match.group())].count('\n') + 1,
            'sha256': digest(match.group().encode())})
    core.append({'path': str(rel), 'baseline_sha256': sha(path), 'new_sha256': sha(current),
                 'exact': before == after})
    if before != after:
        deltas.append(''.join(difflib.unified_diff(before.splitlines(True), after.splitlines(True),
                      fromfile='a/' + str(rel), tofile='b/' + str(rel))))
assert len(proofs) == 138
(R / 'core-semantic-integration.diff').write_text('\n'.join(deltas))
oldbody = normalize(native[native.index('\\section{The arithmetic identity and its variables}'):
                           native.index('\\end{document}')].strip())
newbody = chapter[chapter.index('\\section{The arithmetic identity and its variables}'):
                  chapter.index('\\section{Finite matrix kernels and positive trace}')].strip()
newbody = re.sub(r'\\Needspace\{[57]\\baselineskip\}\n', '', newbody)
newbody = newbody.replace('For the $*$-algebras in this chapter, a unit is a nonzero element $1$\nwith $1a=a1=a$ for every $a$;',
                          'A unit is a nonzero element $1$ with $1a=a1=a$ for every $a$;')
assert oldbody == newbody, 'Undeclared native body change'
new_proofs = []
native_blocks = {normalize(m.group()) for m in re.finditer(proof_pattern, native, re.S)}
for match in re.finditer(proof_pattern, chapter, re.S):
    if match.group() not in native_blocks:
        new_proofs.append({'start_line': chapter[:match.start()].count('\n') + 1,
                           'end_line': chapter[:match.end()].count('\n') + 1,
                           'sha256': digest(match.group().encode())})
assert len(new_proofs) == 4
save('proof-correspondence.json', {'native': rows, 'core_files': core, 'core_proofs': proofs,
     'new_proofs': new_proofs, 'all_33_native_preserved': True, 'all_138_core_proofs_exact': True,
     'entire_native_body_preserved_under_declared_transport': True,
     'transport': ['von Mangoldt math-font subscript', 'chapter-scoped nonzero unit convention',
                   'Needspace pagination declarations'],
     'scope': 'Complete proof-byte correspondence and semantic transport check. This is not a fresh acceptance of all inherited theorems.'})

alltex = '\n'.join(p.read_text() for p in sorted(S.rglob('*.tex')))
labels = re.findall(r'\\label\{([^}]+)\}', alltex)
refs = re.findall(r'\\(?:eqref|ref|pageref|autoref)\{([^}]+)\}', alltex)
assert len(labels) == len(set(labels)) == 799
assert not set(refs) - set(labels)
firewall = r'(?i)\b(?:worktree|checkpoint|reviewer|audit|TODO|acceptance|Codex|Fable)\b|/Users/|~/|kernel/formal|kernel/docs|centcom/'
assert not re.search(firewall, alltex)
assert '%' not in chapter and not re.search(r'\\(?:input|include|cite|bibliography|bibitem)\b', chapter)
assert sha(S / 'raeez-math-template.sty') == '07336dc2503195a619a5b566e8730e891d4c81b2465530873214d7087b83e4b5'

pdfs = []
copydir = R / 'input-by-sha256'
copydir.mkdir(exist_ok=True)
for kind, job in [('full', 'programme'), ('standalone', 'weil-standalone'), ('baseline', 'programme')]:
    build = R / ('build-' + kind)
    source = C / 'baseline-source' if kind == 'baseline' else S
    pdf, fls, log = [build / (job + '.' + ext) for ext in ['pdf', 'fls', 'log']]
    logtext = log.read_text(errors='replace')
    assert not re.search(r'undefined|multiply defined|Overfull|Underfull|destination.*does not exist', logtext)
    warnings = [line for line in logtext.splitlines() if 'Warning' in line]
    assert warnings == ['Package epstopdf Warning: Shell escape feature is not enabled.'], warnings
    paths = {(source / line[6:]).resolve() for line in fls.read_text().splitlines() if line.startswith('INPUT ')}
    inputs = []
    for p in sorted(paths):
        h = sha(p)
        target = copydir / h
        if not target.exists():
            shutil.copyfile(p, target)
        assert sha(target) == h
        inputs.append({'path': str(p), 'sha256': h, 'bytes': p.stat().st_size,
                       'preserved_copy': str(target.relative_to(R)), 'generated': p.parent == build})
    save('build-inputs-' + kind + '.json', inputs)
    doc = fitz.open(pdf)
    text = '\n'.join(p.get_text() for p in doc)
    reader = PdfReader(pdf)
    assert not re.search(firewall, text)
    assert not re.search(firewall, ' '.join(str(v) for v in reader.metadata.values()))
    (R / (kind + '.txt')).write_text(text)
    fonts = subprocess.run(['pdffonts', str(pdf)], capture_output=True, text=True, check=True).stdout
    (R / ('fonts-' + kind + '.txt')).write_text(fonts)
    assert all(re.search(r'\byes\s+yes\s+yes\s+\d+\s+\d+\s*$', line) for line in fonts.splitlines()[2:])
    pdfs.append({'kind': kind, 'path': str(pdf.relative_to(W)), 'sha256': sha(pdf), 'pages': len(doc),
                 'fls_sha256': sha(fls), 'log_sha256': sha(log), 'build_inputs': len(inputs),
                 'warnings': warnings, 'all_fonts_embedded_subset_unicode': True})

for name, assets in [('full-reader-sources.zip', sorted(p for p in S.rglob('*') if p.is_file())),
                     ('standalone-reader-sources.zip', [S / 'weil-standalone.tex', S / 'raeez-math-template.sty',
                                                       S / 'manuscript/weil-forms-and-domains.tex'])]:
    with zipfile.ZipFile(R / name, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        for p in assets:
            info = zipfile.ZipInfo(str(p.relative_to(S)), date_time=(2026, 9, 14, 0, 0, 0))
            info.external_attr = 0o644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, p.read_bytes())
    with zipfile.ZipFile(R / name) as archive:
        for member in archive.namelist():
            assert digest(archive.read(member)) == sha(S / member)
save('verification-results.json', {'status': 'Source and diagnostic checks passed; root acceptance remains required',
     'pdfs': pdfs, 'source_labels': 799, 'source_and_pdf_firewall': True,
     'native_proofs_retained': 33, 'core_proofs_exact': 138, 'new_proofs': 4})
save('tool-versions.json', {'python': sys.version, 'python_binary': sys.executable,
     'pymupdf': fitz.VersionBind, 'pypdf': __import__('pypdf').__version__,
     'pdflatex': subprocess.check_output(['pdflatex', '--version'], text=True),
     'latexmk': subprocess.check_output(['latexmk', '--version'], text=True)})
print(json.dumps({'source_assets': 26, 'labels': 799, 'pdfs': pdfs}))
