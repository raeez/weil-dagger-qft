from pathlib import Path
import subprocess,json
import fitz
R=Path(__file__).resolve().parent;W=R.parents[3];S=W/'research-candidates/weil-core019';d=R/'reference-probes';d.mkdir(exist_ok=True)
variants={'late_false':('',r'\mathtoolsset{showonlyrefs=false}'),'early_false':(r'\mathtoolsset{showonlyrefs=false}',''),'early_false_toggle':(r'\mathtoolsset{showonlyrefs=false}',r'\mathtoolsset{showonlyrefs=true}\mathtoolsset{showonlyrefs=false}'),'early_false_group':(r'\mathtoolsset{showonlyrefs=false}',r'\begingroup\mathtoolsset{showonlyrefs=true}Old text.\par\endgroup')}
rows=[]
for name,(early,late) in variants.items():
 p=d/(name+'.tex');p.write_text('\\documentclass{memoir}\n\\usepackage{raeez-math-template}\n'+early+'\n\\begin{document}\n'+late+'\n\\begin{equation}x=1\\label{eq:probe}\\end{equation}\nReference \\eqref{eq:probe}, ordinary \\ref{eq:probe}.\n\\end{document}\n')
 for _ in range(2):
  cp=subprocess.run(['pdflatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error',f'-output-directory={d}',str(p)],cwd=S,capture_output=True,text=True)
  assert cp.returncode==0,cp.stdout[-2000:]
 txt='\n'.join(p.get_text() for p in fitz.open(d/(name+'.pdf')))
 rows.append(dict(variant=name,text=txt));print(name,repr(txt))
(R/'reference-probe-results.json').write_text(json.dumps(rows,indent=2)+'\n')
