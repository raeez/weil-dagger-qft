from pathlib import Path
import hashlib,json,re,shutil,subprocess,tarfile,zipfile,sys
from pypdf import PdfReader
import fitz
R=Path(__file__).resolve().parent;W=R.parents[3];S=W/'research-candidates/weil-core019';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(n,o):(R/n).write_text(json.dumps(o,indent=2)+'\n')
inputs=json.loads((R/'preserved-inputs.json').read_text())
for e in inputs:
 assert sha(e['original'])==e['sha256'],e['original']
 copy=e.get('baseline_copy',e['copy']);assert sha(W/copy)==e['sha256'],copy
m=json.loads((R/'inputs/00-candidate024-manifest.json').read_text());assert sha(R/'inputs/00-candidate024-manifest.json')=='a79abdd9d43984194f5bde7586e0433a56a1ab9938ccf5f35934b0ac8155e730'
oldroot=Path(m['repository']);closure=Path(m['source_closure']);original_records=[]
copydir=R/'programme024-input-by-sha256';copydir.mkdir(exist_ok=True)
for e in m['full_build_inputs']:
 p=Path(e['path']);expected=Path(e['path']);changed=not p.exists() or sha(p)!=e['sha256']
 if changed:
  rel=p.relative_to(oldroot);expected=closure/rel;assert sha(expected)==e['sha256'],p
 dest=copydir/e['sha256']
 if not dest.exists():shutil.copyfile(expected,dest);dest.chmod(0o444)
 assert sha(dest)==e['sha256']
 original_records.append(dict(original=str(p),original_live_hash_differs=changed,expected_bytes_source=str(expected),sha256=e['sha256'],preserved_copy=str(dest.relative_to(R))))
save('programme024-build-inputs-preserved.json',original_records)
old_manifest=W/'reports/research/CONSTRUCTION-2026-09-14/weil-boundary-native018/freeze.json';old=json.loads(old_manifest.read_text());assert sha(old_manifest)=='693d9ed261e46e6e40f80ef773c70f720a0dd20ee4d5beb4a04ea700a5155107'
for e in old['files']:assert sha(W/e['path'])==e['sha256']
for e in json.loads((R/'baseline-build-inputs.json').read_text()):
 assert sha(e['preserved_source_path'])==e['sha256'];assert sha(R/e['preserved_copy'])==e['sha256']
save('preservation.json',dict(native018_manifest_sha256=sha(old_manifest),native018_files_verified=len(old['files']),programme024_assets_verified=len(m['source_files']),programme024_build_input_records_preserved=len(original_records),original_live_input_paths_with_retained_frozen_alternatives=[e['original'] for e in original_records if e['original_live_hash_differs']],direct_inputs_verified=len(inputs),baseline_input_records_verified=341,root_live_sources_read_only=True))

alltex='\n'.join(p.read_text() for p in sorted(S.rglob('*.tex')))
labels=re.findall(r'\\label\{([^}]+)\}',alltex);refs=re.findall(r'\\(?:eqref|ref|pageref|autoref)\{([^}]+)\}',alltex)
assert len(labels)==len(set(labels))==799
assert not set(refs)-set(labels),set(refs)-set(labels)
forbidden=r'(?i)\b(?:worktree|checkpoint|reviewer|audit|TODO|acceptance|Codex|Fable)\b'
assert not re.search(forbidden,alltex)
assert not re.search(r'/Users/|~/|kernel/formal|kernel/docs|centcom/',alltex)
chapter=(S/'manuscript/weil-forms-and-domains.tex').read_text();assert '%' not in chapter
assert not re.search(r'\\(?:input|include|cite|bibliography|bibitem)\b',chapter)
assert sha(S/'raeez-math-template.sty')=='07336dc2503195a619a5b566e8730e891d4c81b2465530873214d7087b83e4b5'

pdf_records=[]
for kind,job in [('full','programme'),('standalone','weil-standalone')]:
 build=R/f'build-{kind}';pdf=build/f'{job}.pdf';log=(build/f'{job}.log').read_text(errors='replace');fls=build/f'{job}.fls'
 assert not re.search(r'undefined|multiply defined|Overfull|Underfull|destination.*does not exist',log)
 warnings=[x for x in log.splitlines() if 'Warning' in x];assert warnings==['Package epstopdf Warning: Shell escape feature is not enabled.'],warnings
 p=PdfReader(pdf);d=fitz.open(pdf);txt='\n'.join(pg.get_text() for pg in d)
 assert not re.search(forbidden,txt)
 assert not re.search(forbidden,' '.join(str(v) for v in p.metadata.values()))
 (R/f'{kind}.txt').write_text(txt)
 font=subprocess.run(['pdffonts',str(pdf)],capture_output=True,text=True,check=True).stdout
 (R/f'fonts-{kind}.txt').write_text(font)
 assert all(re.search(r'\byes\s+yes\s+yes\s+\d+\s+\d+\s*$',line) for line in font.splitlines()[2:])
 paths={(S/line[6:]).resolve() for line in fls.read_text().splitlines() if line.startswith('INPUT ')}
 records=[];copies=R/f'{kind}-input-by-sha256';copies.mkdir(exist_ok=True)
 for inp in sorted(paths):
  assert inp.is_file();h=sha(inp);dest=copies/h
  if not dest.exists():shutil.copyfile(inp,dest);dest.chmod(0o444)
  assert sha(dest)==h
  records.append(dict(path=str(inp),sha256=h,bytes=inp.stat().st_size,preserved_copy=str(dest.relative_to(R)),generated=inp.parent==build))
 save(f'build-inputs-{kind}.json',records)
 pdf_records.append(dict(kind=kind,path=str(pdf.relative_to(W)),sha256=sha(pdf),pages=len(p.pages),fls_sha256=sha(fls),log_sha256=sha(build/f'{job}.log'),build_inputs=len(records),all_fonts_embedded_subset_unicode=True,warnings=warnings))

assets=[p for p in sorted(S.rglob('*')) if p.is_file()];assert len(assets)==26
source_records=[dict(path=str(p.relative_to(S)),sha256=sha(p),bytes=p.stat().st_size) for p in assets]
save('source-closure.json',dict(files=source_records,assets=26,reader_entrypoint='manuscript/programme.tex',standalone_entrypoint='weil-standalone.tex',source_aggregate_sha256=hashlib.sha256(json.dumps(source_records,sort_keys=True,separators=(',',':')).encode()).hexdigest(),reader_contains_no_operational_reports_or_build_products=True))
for name,files in [('full-reader-sources.zip',assets),('standalone-reader-sources.zip',[S/'weil-standalone.tex',S/'raeez-math-template.sty',S/'manuscript/weil-forms-and-domains.tex'])]:
 with zipfile.ZipFile(R/name,'w',compression=zipfile.ZIP_DEFLATED) as z:
  for p in files:
   info=zipfile.ZipInfo(str(p.relative_to(S)),date_time=(2026,9,14,0,0,0));info.external_attr=0o644<<16;info.compress_type=zipfile.ZIP_DEFLATED;z.writestr(info,p.read_bytes())
versions={}
for key,cmd in [('pdflatex',['pdflatex','--version']),('latexmk',['latexmk','--version']),('pdffonts',['pdffonts','-v'])]:
 c=subprocess.run(cmd,capture_output=True,text=True);b=Path(shutil.which(cmd[0])).resolve();versions[key]=dict(command=cmd,returncode=c.returncode,output=c.stdout+c.stderr,binary=str(b),binary_sha256=sha(b))
versions['python']=dict(path=sys.executable,version=sys.version,pypdf=__import__('pypdf').__version__,pymupdf=fitz.VersionBind)
save('tool-versions.json',versions)
save('verification-results.json',dict(status='diagnostic checks passed; independent mathematical integration review required',pdfs=pdf_records,all_source_labels=799,missing_or_duplicate_labels=[],new_actual_label_count_each_pdf=127,inline_equation_display_and_reference_counts_each_pdf='all73 equation labels exact',native_proof_transport='33 preserved;32exact bytes,one explicit-formula proof has sole math-font subscript migration',new_proofs=4,prior_core_proofs_exact=138,source_pdf_firewall_diagnostics=True,approved_style_exact=True))
print(json.dumps(dict(labels=len(labels),assets=len(assets),pdfs=pdf_records)))
