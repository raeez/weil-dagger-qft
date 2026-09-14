from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys

report = Path(__file__).resolve().parent
worktree = report.parents[3]
kind = sys.argv[1]
source = worktree / 'research-candidates/weil-core020'
entry = 'manuscript/programme.tex'
job = 'programme'
if kind == 'standalone':
    entry = 'weil-standalone.tex'
    job = 'weil-standalone'
elif kind == 'baseline':
    source = report / 'custody019/baseline-source'
elif kind != 'full':
    raise ValueError(kind)
output = report / ('build-' + kind)
output.mkdir(exist_ok=True)
environment = os.environ.copy()
environment.update(SOURCE_DATE_EPOCH='1789344000', FORCE_SOURCE_DATE='1', TZ='UTC')
command = ['latexmk', '-norc', '-g', '-pdf', '-recorder',
           '-pdflatex=pdflatex -no-shell-escape %O %S',
           '-interaction=nonstopmode', '-halt-on-error', '-outdir=' + str(output), entry]
records = []
for attempt in [1, 2]:
    logfile = report / f'build-{kind}-pass{attempt}.log'
    with logfile.open('w') as stream:
        result = subprocess.run(command, cwd=source, env=environment, stdout=stream, stderr=subprocess.STDOUT)
    row = {'attempt': attempt, 'command': command, 'cwd': str(source),
           'environment': {k: environment[k] for k in ['SOURCE_DATE_EPOCH', 'FORCE_SOURCE_DATE', 'TZ']},
           'returncode': result.returncode, 'log': logfile.name,
           'log_sha256': hashlib.sha256(logfile.read_bytes()).hexdigest()}
    if result.returncode:
        records.append(row)
        (report / f'build-{kind}.json').write_text(json.dumps(records, indent=2) + '\n')
        raise SystemExit(result.returncode)
    row['pdf_sha256'] = hashlib.sha256((output / (job + '.pdf')).read_bytes()).hexdigest()
    records.append(row)
(report / f'build-{kind}.json').write_text(json.dumps(records, indent=2) + '\n')
assert records[0]['pdf_sha256'] == records[1]['pdf_sha256'], 'PDF did not converge'
print(kind, records[-1]['pdf_sha256'], 'two converged latexmk runs')
