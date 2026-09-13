from pathlib import Path
import hashlib,json,re,shutil
root=Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest()
recovery=Path('/Users/raeez/mathematics/worktrees/frontier-recovery-astra-ultra-20260913/reports/research/RECOVERY-2026-09-13')
cat=Path('/Users/raeez/mathematics/worktrees/frontier-catalogue-20260913/reports/research/COVERAGE-2026-09-13/files.jsonl')
index={x['sha256']:x for x in map(json.loads,cat.read_text().splitlines())}
sources={}
def source(key,path,spans):
 p=Path(path); b=p.read_bytes(); lines=b.splitlines(keepends=True)
 dest=root/'sources'/f'{key}{p.suffix}'
 if dest.resolve()!=p.resolve():dest.write_bytes(b)
 anchors=[]
 for a,z in spans:
  lo=sum(map(len,lines[:a-1]));hi=sum(map(len,lines[:z]))
  anchors.append({'lines':[a,z],'bytes':[lo,hi],'sha256':sha(b[lo:hi])})
 sources[key]={'path':str(p),'sha256':sha(b),'snapshot':str(dest.relative_to(root.parent.parent.parent)), 'anchors':anchors}
source('base-paper',root/'baseline/paper.tex',[(1,617)])
source('return-sw002-g02-p03',recovery/'returns/sw002_g02--p03-final-01.md',[(7,91),(95,124),(132,140),(205,208)])
source('return-cr-g08-p004',recovery/'returns/critique_groups_02_08--g08--p004-final-01.md',[(118,191),(270,322)])
source('return-cr-g05-s001',recovery/'returns/critique_groups_02_08--g05--s001-final-01.md',[(170,200)])
source('synthesis-arithmetic','/Users/raeez/mathematics/worktrees/full-synthesis-integration-20260909/reports/research/FULL-SYNTHESIS-2026-09-09/source/modules/arithmetic.tex',[(1535,1658),(1659,1723)])
for key,h,spans in [
 ('historical-platonic','bc9bea5959381262b0d664ba161b95da323b405293553c3b09ccaf5e042446be',[(526,704)]),
 ('historical-recap','81bd9faaac3bfb146ee481f0e924a7f4d193737d7d5d79d79a59a45fad7f726c',[(114,136)]),
 ('historical-weil-seed','298768f86e8c43f303c63a766ddfd4d930a465f7b1fea8adbb5f36b21a69a806',[(1,38)]),
 ('archived-kms','a704b37a946dca47ad1497085cd484bb20f34e171194078d1cc1ea74afef64f0',[(237,440)]),
 ('archived-gaussians','5120bfcfbc251446d363cdb7196b89b3cf024e814863bc32c92ffedc4956eb4b',[(301,617)]),
 ('archived-copoisson','7706234b140a21fb772d9f031aa3e4970383513e2d9660c9655af376417336dd',[(396,578)])]:
 p=index[h]['canonical']; assert sha(Path(p).read_bytes())==h;source(key,p,spans)
# Retain every public assistant message in the relevant prior threads. Do not
# extract analysis messages or claim unavailable reasoning was recovered.
manifest=json.loads((recovery/'returns-manifest-049.json').read_text())
threads=[]
for e in manifest['entries']:
 if e['task'] in ['/root/sw002_g02/p03','/root/critique_groups_02_08/g08/p004','/root/critique_groups_02_08/g05/s001']:
  p=Path(e['source']); records=[]
  for i,l in enumerate(p.read_bytes().splitlines(keepends=True),1):
   x=json.loads(l); q=x.get('payload',{})
   if x.get('type')=='response_item' and q.get('type')=='message' and q.get('role')=='assistant' and q.get('channel')!='analysis':
    content='\n'.join(c.get('text','') for c in q.get('content',[]))
    records.append({'source_line':i,'record_sha256':sha(l),'channel':q.get('channel'),'text':content})
  name=e['task'].replace('/','--').strip('-')+'-public.json'
  (root/'sources'/name).write_text(json.dumps(records,indent=2)+'\n')
  threads.append({'source':str(p),'source_sha256':sha(p.read_bytes()),'snapshot':'sources/'+name,'record_count':len(records),'limit':'Only public assistant messages retained. Supplemental non-Weil turns are preserved, not mathematically certified.'})
items=[]
def item(id,claim,origin,status,dest,evidence,residual='None for the stated result; independent candidate review remains required.'):
 items.append(dict(id=id,claim=claim,source_keys=origin,status=status,destination=dest,evidence=evidence,residual_obligation=residual))
item('W01','Nonunital square positivity gives GNS left ideal, closability and exact boundedness condition.',['base-paper','synthesis-arithmetic','return-sw002-g02-p03','return-cr-g08-p004'],'retained-and-reproved','paper.tex thm:gns','Cauchy-Schwarz applied to b and a*ab; dense adjoint domain.')
item('W02','A common invariant closed representation is available after algebraic GNS.',['base-paper'],'implemented-with-complete-proof','paper.tex thm:graph-domain','For every finite F, c=sum a*a controls the graph seminorms. This proves simultaneous approximation, intersection equality, invariance, exact products and minimality. Powers Definition 2.4 and Lemma 2.6 independently checked in the retained primary preprint.')
item('W03','The maximal domain of one closed multiplier form is invariant.',['base-paper','return-sw002-g02-p03'],'contradicted-with-deciding-example','paper.tex ex:maximal-domain','N on l2: v_n=n^-2 has sum n²|v_n|² finite but sum n⁴|v_n|² infinite. All-moment domain is invariant.')
item('W04','Dagger isometry extends to closed common domains.',['synthesis-arithmetic','return-sw002-g02-p03'],'implemented-with-exact-carrier','paper.tex prop:graph-transfer; ex:transfer-domain','Unitarily transport each graph in the closed Hilbert range; ambient closures give inclusion. The c00 subset C[n]+c00 weighted example disproves full-target domain equality.')
item('W05','Full Weil functional admits no finite positive unitization.',['return-sw002-g02-p03'],'integrated-and-strengthened','paper.tex thm:weil-mass; cor:weil-carriers','Local Gaussian asymptotic with explicit leading coefficient, prime exponential bound, DLMF digamma estimate, divergent representability ratio. No RH used.')
item('W06','Nontrivial positive Gaussian test subspaces can be constructed.',['historical-weil-seed','archived-gaussians'],'implemented-with-new-finite-family-proof','paper.tex thm:gaussian-subspaces','Normalized Gram matrices converge to the positive Gram matrix ((lambda_j+lambda_k)^(-1/2)); for scales 1,4 the determinant is 1/20.','No uniform threshold over all finite families; no positivity on the whole algebra; no independent state realizing the full functional.')
item('W07','The unconditional Hermitian radical quotient carries left convolution.',['historical-platonic','historical-recap'],'integrated-in-correct-carrier','paper.tex Section 7','B(af,g)=B(f,a*g) proves left-ideal invariance. Hermiticity makes the quotient nondegenerate. A Hilbert or Krein topology is not produced.')
item('W08','Adjoining a positive unit and its cyclic vector follows from RH.',['historical-platonic','historical-recap'],'contradicted-and-repaired','paper.tex thm:weil-mass; thm:gns','A finite positive unit would obey the impossible Gaussian unitization bound. The nonunital GNS quotient survives under Weil positivity.','Arithmetic positivity remains open. No repair can retain a finite vector representing the full functional on this algebra.')
item('W09','A square-positive functional can have zero GNS space despite being nonzero.',['synthesis-arithmetic','return-sw002-g02-p03'],'retained-developer-example','reports/research/MINING-2026-09-13/REPORT.md','A=Cx, x*=x, x²=0, L(x)=1. All square values vanish; L is nonzero. The stronger actual-Weil obstruction is in the paper.')
item('W10','Sharp C*-unitization and approximate-identity theorem.',['base-paper','synthesis-arithmetic','return-sw002-g02-p03'],'retained','paper.tex thm:cstar-unitization','Quadratic minimization and C*-positive-functional boundedness supply m>=norm(omega); approximate identities give the minimal vector.','No new primary Segal scan obtained in this phase; inherited locator requires source lane verification on the exact candidate.')
item('W11','Symmetric closable operators need not admit self-adjoint extensions.',['base-paper','synthesis-arithmetic','return-sw002-g02-p03'],'retained-and-expanded','paper.tex Section 2','Half-line momentum deficiency equations give e^-x and e^x, hence indices (1,0).')
item('W12','Indefinite adjoints and isotropic quotients imply positivity.',['base-paper','historical-platonic'],'contradicted-with-retained-examples','paper.tex Section 7','J=diag(1,-1), X=e21 gives -1. Isotropic vectors e1+e2 and e1-e2 sum to a non-isotropic vector.')
item('W13','Positive functional identity fixes spectral multiplicity.',['return-sw002-g02-p03'],'contradicted-and-integrated','paper.tex final paragraph','W(z)=mz has one-dimensional GNS space; scalar trace realization in dimension m has determinant multiplicity m.','A spectral determinant needs an independent carrier/domain/multiplicity theorem.')
item('W14','Full-domain Deninger identity and exact determinant comparison imply RH.',['historical-platonic','synthesis-arithmetic','return-sw002-g02-p03'],'retained-conditional-cross-repository-obligation','reports/research/MINING-2026-09-13/REPORT.md','Theta*=I-Theta with equality of domains makes -i(Theta-1/2) self-adjoint. No such arithmetic Theta is constructed.','Arithmetic cohomology and determinant construction are outside this paper phase; parent owns cross-repository propagation.')
item('W15','Archived Bost-Connes state gives a positive Weil comparison.',['archived-kms','return-cr-g08-p004'],'contradicted-at-first-defining-relation','reports/research/MINING-2026-09-13/REPORT.md','At gamma=0, m=n>1, the stated relation mu_m*mu_m=1 conflicts with phi(mu_m*mu_m)=1/m and phi(1)=1. The proposed state is not a functional.','A consistent KMS state and modular domains must be constructed by the Volume IV owner. Even a correct C*-state cannot pull back to the full Weil functional, by cor:weil-carriers.')
item('W16','Balanced Gaussian explicit formula proves positivity.',['archived-gaussians'],'carrier-distinction-preserved-and-positive-subclass-constructed','paper.tex eq:weil-functional; thm:gaussian-subspaces','The archived W subtracts the zero sum and is claimed identically zero. It differs from the full arithmetic L_zeta here. Its Gaussian convolution identity is valid after normalization; a zero balanced identity is no positivity proof.','The archived Fourier/prime/gamma normalization has not been certified. No finite-part gamma identity is imported. The retained paper uses an absolutely convergent real-frequency gamma integral.')
item('W17','Co-Poisson conditions CP1-CP3 define a possible nonempty subclass.',['archived-copoisson'],'ordinary-integral-domain-refuted','reports/research/MINING-2026-09-13/REPORT.md','For nonzero f in L2, its autocorrelation phi is continuous and phi(0)=norm(f)^2>0. Thus integral_0^delta Re(phi(y)) dy/y diverges, contrary to CP1. CP3 itself restates the intended inequality.','A subtracted or regularized Mellin mean is a different construction. Its exact formula, cutoff dependence, comparison and positivity remain unresolved; no nonemptiness claim is imported.')
item('W18','All finite-rank operators lie in the range a rho^(1/2).',['return-cr-g08-p004'],'retained-counterexample-and-correct-density-route','reports/research/MINING-2026-09-13/REPORT.md','rho_n=const n^-beta; v_n=n^(-(beta+1)/2) gives a rank-one map outside the range because rho^(-1/2)v is not l2. Finite matrix units remain in the range and are HS dense.','Volume IV owns implementation; no Hilbert-Schmidt range equality is used here.')
item('W19','Public unfinished and intermediate Weil/GNS claims from the relevant retained sessions.',['return-sw002-g02-p03','return-cr-g08-p004','return-cr-g05-s001'],'preserved-and-classified','sources/*-public.json','Public commentary includes the earlier RH-conditional finite-mass claim. The later local-term proof is stronger and is integrated. Other visible messages introduce no additional completed domain theorem.','No missing private or unsaved reasoning reconstructed. Whole-corpus mining and unrelated supplemental turns are not certified by this bounded phase.')
(root/'mining-dispositions.json').write_text(json.dumps({'schema':1,'scope':'Bounded Weil/GNS source implementation, with every recovered relevant argument and known residual preserved. This is not whole-corpus acceptance.','base_commit':'cce2bc383bcf2fd930e917a5abb773e0469465cc','requested_controls':{'model':'gpt-6-astra','reasoning_effort':'ultra','observed_runtime_metadata':'unverified'},'source_policy':'Archives and returns are discovery material; exact proofs and primary sources establish the candidate mathematics.','sources':sources,'public_threads':threads,'dispositions':items},indent=2)+'\n')
print('Recorded',len(sources),'exact source snapshots and',len(items),'claim dispositions.')
