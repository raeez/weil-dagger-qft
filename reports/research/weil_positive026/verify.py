"""Bind the source closure, retained arithmetic chapter, and rendered appendix."""

from pathlib import Path
import hashlib
import json
import re
import subprocess

import fitz


report = Path(__file__).resolve().parent
root = report.parents[2]
manifest = json.loads((report/'source-manifest.json').read_text())
for row in manifest['source_files']:
    data = (root/row['path']).read_bytes()
    assert hashlib.sha256(data).hexdigest() == row['sha256'], row['path']

baseline_source = (report/'inputs/arithmetic.tex').read_bytes()
assert hashlib.sha256(baseline_source).hexdigest() == (
    '56b73a14e153c3405d29e9b842919d6576cff110d17175a2e999443745d17112')
assert baseline_source.count(b'\\begin{proof}') == 39

source = (root/'research-candidates/weil_positive026/prime-difference-carrier.tex').read_text()
labels = re.findall(r'\\label\{([^}]+)\}', source)
assert len(labels) == len(set(labels))
inherited_labels = set(re.findall(r'\\label\{([^}]+)\}', baseline_source.decode()))
assert not inherited_labels.intersection(labels)
refs = set(re.findall(r'\\(?:eqref|ref)\{([^}]+)\}', source))
assert refs <= inherited_labels.union(labels)
firewall = re.compile(r'\b(agent|worktree|workflow|TODO|reviewer|audit|commit|sprint|task packet)\b', re.I)
assert not firewall.search(source)
assert '/Users/' not in source and 'github.com/' not in source

logs = {}
bad_log = re.compile(r'undefined|multiply defined|Overfull|Underfull|LaTeX Warning|Fatal error|^!', re.I | re.M)
for name in ['baseline', 'candidate']:
    log = (report/f'build-{name}/{name}.log').read_text(errors='replace')
    assert not bad_log.search(log), bad_log.findall(log)
    logs[name] = {'sha256': hashlib.sha256(log.encode()).hexdigest(), 'warnings': []}

base_pdf = fitz.open(report/'build-baseline/baseline.pdf')
candidate_pdf = fitz.open(report/'build-candidate/candidate.pdf')
assert len(base_pdf) == 38
assert len(candidate_pdf) == 45
inherited_pages = []
for number, (old, new) in enumerate(zip(base_pdf, candidate_pdf), 1):
    text_match = old.get_text() == new.get_text()
    old_pixels = old.get_pixmap(matrix=fitz.Matrix(1.25, 1.25), alpha=False).samples
    new_pixels = new.get_pixmap(matrix=fitz.Matrix(1.25, 1.25), alpha=False).samples
    pixel_match = old_pixels == new_pixels
    assert text_match and pixel_match, number
    inherited_pages.append({'page': number, 'text_identical': text_match,
                            'raster_identical': pixel_match,
                            'raster_sha256': hashlib.sha256(new_pixels).hexdigest()})

new_pages = []
for number in range(38, len(candidate_pdf)):
    page = candidate_pdf[number]
    text = page.get_text()
    assert len(text) > 1000, number + 1
    assert not firewall.search(text), number + 1
    boxes = [item[:4] for item in page.get_text('blocks')]
    assert all(x0 >= 0 and y0 >= 0 and x1 <= page.rect.width and y1 <= page.rect.height
               for x0, y0, x1, y1 in boxes), number + 1
    new_pages.append({'page': number + 1, 'text_characters': len(text),
                      'all_text_inside_page': True})
assert 'Positive arithmetic forms from prime translations' in candidate_pdf[38].get_text()

pdf_path = report/'build-candidate/candidate.pdf'
font_output = subprocess.check_output(['pdffonts', str(pdf_path)], text=True)
(report/'build-candidate/fonts.txt').write_text(font_output)
font_rows = [row for row in font_output.splitlines()[2:] if row.strip()]
assert font_rows and all(row.split()[-5:-2] == ['yes', 'yes', 'yes'] for row in font_rows)
pdf_info = subprocess.check_output(['pdfinfo', str(pdf_path)], text=True)
(report/'build-candidate/pdfinfo.txt').write_text(pdf_info)
result = {
    'source_aggregate_sha256': manifest['source_aggregate_sha256'],
    'source_closure_verified': True,
    'inherited_proofs_retained': 39,
    'new_proofs': source.count('\\begin{proof}'),
    'labels_valid': True,
    'firewall_scan': 'No prohibited prose or repository paths in the new mathematical module.',
    'build_logs': logs,
    'baseline_pages': len(base_pdf),
    'candidate_pages': len(candidate_pdf),
    'candidate_pdf_sha256': hashlib.sha256(pdf_path.read_bytes()).hexdigest(),
    'inherited_pages': inherited_pages,
    'new_pages': new_pages,
    'visual_review_scope': 'Pages 38 through 45, including the inherited transition. Visual conclusions are recorded separately.',
    'independent_mathematical_acceptance': 'Not established by these checks.'
}
(report/'verification-results.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({k: v for k, v in result.items() if k not in ['inherited_pages', 'new_pages']}, indent=2))
