from pathlib import Path
import fitz,hashlib,json,re
from pypdf import PdfReader
R=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
old=fitz.open(R/'inputs/01-programme.pdf');base=fitz.open(R/'baseline-build/programme.pdf');full=fitz.open(R/'build-full/programme.pdf');stand=fitz.open(R/'build-standalone/weil-standalone.pdf')
def raster(p,body=False):
 rect=fitz.Rect(0,82,p.rect.width,p.rect.height-50) if body else p.rect
 return hashlib.sha256(p.get_pixmap(matrix=fitz.Matrix(1.5,1.5),clip=rect,alpha=False).samples).hexdigest()
assert len(old)==len(base)==320
baseline=[]
for i in range(320):
 assert raster(old[i])==raster(base[i]),i+1
 baseline.append(dict(page=i+1,raster_sha256=raster(base[i])))
basehash=[raster(p) for p in base];fullhash=[raster(p) for p in full]
same=[i+1 for i in range(320) if basehash[i]==fullhash[i]]
changed=[i+1 for i in range(320) if basehash[i]!=fullhash[i]]
body_same=[i+1 for i in range(320) if raster(base[i],True)==raster(full[i],True)]
print('baseline exact320; inherited full page same',len(same),'changed count',len(changed),'first changed',changed[:20])
required=sorted(set(changed+list(range(321,len(full)+1))+[i for n in changed+[321] for i in [n-1,n+1] if 1<=i<=len(full)]))
(R/'render-full').mkdir(exist_ok=True);(R/'render-standalone').mkdir(exist_ok=True)
records={}
for tag,pdf,indices in [('full',full,required),('standalone',stand,list(range(1,len(stand)+1)))]:
 rows=[]
 for n in indices:
  p=R/f'render-{tag}/page-{n:03}.png';pdf[n-1].get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False).save(p);rows.append(dict(page=n,path=str(p.relative_to(R)),sha256=sha(p)))
 records[tag]=dict(pdf_sha256=sha(R/('build-full/programme.pdf' if tag=='full' else 'build-standalone/weil-standalone.pdf')),pages=len(pdf),rendered=rows)
(R/'render-map.json').write_text(json.dumps(records,indent=2)+'\n')
(R/'page-comparison.json').write_text(json.dumps(dict(original_pdf_sha256=sha(R/'inputs/01-programme.pdf'),baseline_pdf_sha256=sha(R/'baseline-build/programme.pdf'),baseline_all320_whole_page_rasters_exact=True,baseline_rasters=baseline,current_pdf_sha256=sha(R/'build-full/programme.pdf'),unchanged_full_pages=same,changed_inherited_pages=changed,unchanged_body_pages=body_same,new_pages=list(range(321,len(full)+1)),rendered_full_pages=required,method='MuPDF1.5 scale; full-page comparison; additional body comparison y82 to height-50'),indent=2)+'\n')
(R/'pre-repeat-pdfs.json').write_text(json.dumps(dict(full=sha(R/'build-full/programme.pdf'),standalone=sha(R/'build-standalone/weil-standalone.pdf')),indent=2)+'\n')
print('Full rendered count',len(required),'standalone',len(stand))
