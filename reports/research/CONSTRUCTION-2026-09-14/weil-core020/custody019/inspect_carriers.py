from pathlib import Path
import re,json,hashlib
from pypdf import PdfReader
import fitz
R=Path(__file__).resolve().parent;W=R.parents[3];S=W/'research-candidates/weil-core019'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def groups(s):
 out=[];d=0;b=0
 for i,c in enumerate(s):
  if c=='{':
   if d==0:b=i+1
   d+=1
  elif c=='}':
   d-=1
   if d==0:out.append(s[b:i])
 return out
source=(S/'manuscript/weil-forms-and-domains.tex').read_text();labels=re.findall(r'\\label\{([^}]+)\}',source)
assert len(labels)==len(set(labels))==127
for kind,job in [('full','programme'),('standalone','weil-standalone')]:
 pdf=R/f'build-{kind}/{job}.pdf';aux=(R/f'build-{kind}/{job}.aux').read_text().splitlines();p=PdfReader(pdf);d=fitz.open(pdf);rows=[];bad=[]
 for label in labels:
  line=next(x for x in aux if x.startswith('\\newlabel{'+label+'}'))
  number,page,title,dest,*_=groups(groups(line)[1]);destination=p.named_destinations[dest];actual=p.get_destination_page_number(destination);target_y=float(d[actual].rect.height)-float(destination.top)
  wanted='('+number+')' if label.startswith('eq:') else number
  hits=[w for w in d[actual].get_text('words') if w[4]==wanted and (not label.startswith('eq:') or w[0]>450)]
  hit=min(hits,key=lambda w:abs((w[1]+w[3])/2-target_y)) if hits else None
  distance=abs((hit[1]+hit[3])/2-target_y) if hit else None
  row=dict(label=label,number=number,aux_page=page,actual_page=actual+1,destination=dest,top=target_y,visible_box=list(hit[:4]) if hit else None,visible_distance=distance,source_line=source[:source.index('\\label{'+label+'}')].count('\n')+1)
  rows.append(row)
  if int(page)!=actual+1 or hit is None or distance>90:bad.append(row)
 (R/f'labels-{kind}.json').write_text(json.dumps(dict(pdf_sha256=sha(pdf),pages=len(p.pages),new_labels=rows,discrepancies=bad),indent=2)+'\n')
 print(kind,'pages',len(p.pages),'new labels',len(rows),'bad',bad)
 print('newchapter begins',rows[0]['actual_page'])

from collections import Counter
source_counts=Counter(re.findall(r"\\eqref\{([^}]+)\}",source))
for kind,job in [('full','programme'),('standalone','weil-standalone')]:
 data=json.loads((R/f'labels-{kind}.json').read_text());start=data['new_labels'][0]['actual_page']-1
 doc=fitz.open(R/f'build-{kind}/{job}.pdf');txt='\n'.join(p.get_text() for p in list(doc)[start:]);out=[]
 for e in data['new_labels']:
  if not e['label'].startswith('eq:'):continue
  expected=1+source_counts[e['label']]
  actual=len(re.findall(re.escape('('+e['number']+')'),txt))
  out.append(dict(label=e['label'],number=e['number'],expected_display_plus_inline_count=expected,actual_pdf_count=actual))
  assert actual==expected,(kind,e['label'],expected,actual)
 (R/f'inline-equations-{kind}.json').write_text(json.dumps(dict(pdf_sha256=sha(R/f'build-{kind}/{job}.pdf'),records=out,all_counts_exact=True),indent=2)+'\n')
 print(kind,'all inline equation-reference counts exact',len(out))
