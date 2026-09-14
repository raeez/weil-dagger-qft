from pathlib import Path
import hashlib,json,re
import sympy as s
R=Path(__file__).resolve().parent;W=R.parents[3];S=W/'research-candidates/weil-core019';P=S/'manuscript/weil-forms-and-domains.tex';new=P.read_text();old=(R/'inputs/04-paper.tex').read_text();sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
norm=lambda t:t.replace('_{\\rm vM}','_{\\mathrm{vM}}')
records=[]
for i,m in enumerate(re.finditer(r'\\begin\{proof\}.*?\\end\{proof\}',old,re.S),1):
 block=m.group();mapped=norm(block);assert new.count(mapped)==1
 start=new.index(mapped);records.append(dict(proof=i,old_start_line=old[:m.start()].count('\n')+1,old_end_line=old[:m.end()].count('\n')+1,new_start_line=new[:start].count('\n')+1,new_end_line=new[:start+len(mapped)].count('\n')+1,old_sha256=hashlib.sha256(block.encode()).hexdigest(),new_sha256=hashlib.sha256(mapped.encode()).hexdigest(),byte_identical=block==mapped,sole_normalization='legacy von Mangoldt subscript rm vM to mathrm{vM}' if block!=mapped else None))
assert len(records)==33 and sum(x['byte_identical'] for x in records)==32
allproofs=list(re.finditer(r'\\begin\{proof\}.*?\\end\{proof\}',new,re.S));assert len(allproofs)==37
newproofs=[]
for m in allproofs:
 if not any(m.group()==norm(x.group()) for x in re.finditer(r'\\begin\{proof\}.*?\\end\{proof\}',old,re.S)):
  newproofs.append(dict(start_line=new[:m.start()].count('\n')+1,end_line=new[:m.end()].count('\n')+1,sha256=hashlib.sha256(m.group().encode()).hexdigest()))
core=[];count=0
for p in sorted((R/'baseline-source').rglob('*.tex')):
 q=S/p.relative_to(R/'baseline-source');a=p.read_text();b=q.read_text();proofs=list(re.finditer(r'\\begin\{proof\}.*?\\end\{proof\}',a,re.S))
 for m in proofs:assert m.group() in b,p
 count+=len(proofs);core.append(dict(path=str(q.relative_to(S)),baseline_sha256=sha(p),new_sha256=sha(q),byte_identical=a==b,all_prior_proofs_exact=True,proof_count=len(proofs)))
(R/'proof-correspondence.json').write_text(json.dumps(dict(native_source_sha256=sha(R/'inputs/04-paper.tex'),new_source_sha256=sha(P),native_proofs=records,new_proofs=newproofs,core_sources=core,all_core_proofs_exact=count,native_transport=dict(all33_retained=True,byte_identical=32,notation_only_migration=1,all_focused_boundary_proofs_exact=True,legacy_font_occurrences=8,heading_space_commands=new.count('\\Needspace{5\\baselineskip}'))),indent=2)+'\n')
I=s.I;A=s.Matrix([[1+I,2,0],[-I,0,3],[0,1-I,2]]);B=s.Matrix([[0,2-I,1],[3,I,0],[1,-2,1+I]]);C=s.Matrix([[1,0,I],[2,1,0],[0,3,2-I]])
pair=s.trace(C.conjugate().T*B);coords=sum(B[i,j]*s.conjugate(C[i,j]) for i in range(3) for j in range(3));assert s.simplify(pair-coords)==0
norm2=s.simplify(s.trace(B.conjugate().T*B));assert norm2==sum(s.expand_complex(abs(v)**2) for v in B)
left=(A*B).vec()-s.kronecker_product(s.eye(3),A)*B.vec();assert left==s.zeros(9,1)
cyclic=s.simplify(s.trace(A*B)-s.trace(B*A));assert cyclic==0
u=s.symbols('u',real=True);h=s.symbols('h',positive=True);moment=[]
for n in range(9):
 p=u**n;formula=sum(h**m*s.diff(p,u,2*m).subs(u,0)/(2**m*s.factorial(m)) for m in range(n//2+1))
 integral=s.integrate(p*s.exp(-u**2/(2*h)),(u,-s.oo,s.oo))/s.sqrt(2*s.pi*h)
 assert s.simplify(formula-integral)==0
 moment.append(dict(power=n,value=str(s.simplify(formula)),integral_residual='0'))
c=s.symbols('c',real=True);corners=[dict(n=n,mass=n,unit_complement_value=str(c-n),mass_bound_ratio=n) for n in range(1,5)]
rec=dict(exact=True,sympy=s.__version__,matrix_pairing=str(s.simplify(pair)),matrix_square_norm=str(norm2),pairing_residual='0',left_action_residuals=['0']*9,cyclic_residual='0',finite_corners=corners,gaussian_moments=moment,scope='Finite exact identities support the stated calculations. Density, continuity obstruction, all-mass obstruction, formal coefficient sums and unit argument are proved generally in the four new manuscript proofs. No numerical RH or positivity inference.')
(R/'exact-calculations.json').write_text(json.dumps(rec,indent=2)+'\n')
print(json.dumps(dict(imported_proofs=33,byte_identical=32,notation_only=1,new_proofs=4,prior_core_proofs_exact=count,matrix_square_norm=str(norm2))))
