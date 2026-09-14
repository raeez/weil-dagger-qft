from pathlib import Path
import hashlib
import json
import re
from pypdf import PdfReader

R = Path(__file__).resolve().parent
S = R.parents[3] / 'research-candidates/weil-core020'
def groups(s):
    out = []
    depth = 0
    start = 0
    for i, c in enumerate(s):
        if c == '{':
            if depth == 0:
                start = i + 1
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                out.append(s[start:i])
    return out

all_results = {}
for kind, source in [('full', S), ('baseline', R / 'custody019/baseline-source')]:
    labels = {}
    for p in sorted(source.rglob('*.tex')):
        text = p.read_text()
        for m in re.finditer(r'\\label\{([^}]+)\}', text):
            labels[m.group(1)] = {'source': str(p.relative_to(source)), 'line': text[:m.start()].count('\n') + 1}
    pdf = R / ('build-' + kind) / 'programme.pdf'
    reader = PdfReader(pdf)
    aux = pdf.with_suffix('.aux').read_text().splitlines()
    mapping = {groups(x)[0]: groups(groups(x)[1]) for x in aux if x.startswith('\\newlabel{')}
    rows, bad = [], []
    for label in labels:
        number, page, title, destination, *_ = mapping[label]
        actual = reader.get_destination_page_number(reader.named_destinations[destination]) + 1
        row = dict(label=label, number=number, aux_page=page, actual_page=actual, destination=destination, **labels[label])
        rows.append(row)
        if int(page) != actual:
            bad.append(row)
    all_results[kind] = {'pdf_sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(), 'rows': rows, 'discrepancies': bad}

baseline = {x['label']: x for x in all_results['baseline']['discrepancies']}
new = []
for row in all_results['full']['discrepancies']:
    old = baseline.get(row['label'])
    if old != row:
        new.append({'current': row, 'baseline': old})
assert len(all_results['full']['discrepancies']) == len(baseline) == 53
assert not new
assert not any(r['source'].endswith('weil-forms-and-domains.tex') for r in all_results['full']['discrepancies'])
all_results['assessment'] = {'all799_destinations_exist': True, 'inherited_discrepancies': 53,
    'new_discrepancies': 0, 'all53_baseline_records_exact': True,
    'scope': 'These navigation discrepancies are retained baseline defects. They do not alter proof bytes, and are not a whole-book acceptance pass.'}
(R / 'all-label-destinations.json').write_text(json.dumps(all_results, indent=2) + '\n')
print('All 799 destinations exist. All 53 discrepancies are exact baseline records. No new discrepancy.')
