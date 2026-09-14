**The mathematical union repair passes for the exact frozen candidate.** One inherited AUX-page discrepancy remains outside the mathematical delta; it prevents claiming that every recorded page value is correct.

This verdict binds:

- Manifest: `91e1f2e14d1819e4439300ad5a0e428b511a99b1bb681cabbdf08109f1c96984`
- Source: `9ef8baa2f0fa7e116646896c454f942830ccd510b9cc7be1d4c3df1ffd0da8c6`
- PDF: `77a4eeda54c4f648b8fb62e258e4134c45ba47c38c77a088a33c54060e6d5205` — 31 pages
- Observed branch/HEAD: `repair/frontier-mine-weil-20260913`, `ba767cd39314b6546b255c98ae16f9d06f261e24`

The GNS bridge at [paper.tex:1260](/Users/raeez/mathematics/worktrees/frontier-mine-weil-20260913/research-candidates/weil-native-integration/candidate002/paper.tex:1260), pp.17–18, closes the previous carrier gap.

Take \(H=L^2(0,\infty;\mathbb C)\), with inner product linear in its first argument, and \(D=C_c^\infty(0,\infty)\). The identity, \(P=-i\,d/dx\), and every \(R_{f,g}x=\langle x,g\rangle f\) preserve \(D\). Integration by parts gives the restricted adjoint identity for \(P\); directly,
\[
\langle R_{f,g}x,y\rangle
=\langle x,g\rangle\langle f,y\rangle
=\langle x,R_{g,f}y\rangle.
\]
Reversing words and conjugating coefficients therefore produces a restricted adjoint for every algebra expression. If an expression represents zero, its proposed adjoint satisfies \(\langle x,B^\dagger y\rangle=0\) for all \(x,y\in D\); density forces \(B^\dagger y=0\). Thus this operation respects every operator relation. Reversal twice gives the identity and reversal of products reverses their order. The actual operator algebra on \(D\) consequently is a complex \(*\)-algebra. Its star is the restriction of the Hilbert adjoint to \(D\), without asserting equality of the full adjoint domains.

For a unit vector \(\Omega\in D\), the functional \(W(B)=\langle B\Omega,\Omega\rangle\) is linear and
\[
W(B^*B)=\|B\Omega\|^2.
\]
Its null space is exactly \(\{B:B\Omega=0\}\), a left ideal. Evaluation induces the isometry
\[
U_0:\mathfrak A_D/\mathcal N_W\longrightarrow D,\qquad [B]\longmapsto B\Omega,
\]
because \(W(C^*B)=\langle B\Omega,C\Omega\rangle\). It is onto since \(R_{f,\Omega}\Omega=f\). Its completion is therefore a unitary onto \(H\), and
\[
U_0\pi_W(C)[B]=CB\Omega=C\,U_0[B].
\]
In particular, the represented \(P\) has **exactly domain \(D\)**. Unitary graph transfer identifies its closure with \(\overline P\).

The unchanged calculation at lines 1220–1258 gives
\[
\ker(P^*-i)=\mathbb C e^{-x},\qquad \ker(P^*+i)=\{0\}.
\]
The first generator has squared norm \(1/2\), while \(e^x\notin H\). Closure preserves the adjoint. A self-adjoint extension on the same Hilbert space would extend the Cayley isometry to a unitary, requiring equal dimensions of the two range complements. Their dimensions \(1\) and \(0\) exclude it. Thus the example now establishes the asserted failure for a symmetric GNS multiplier itself.

The zero-algebra repair is consistent throughout its consumers:

- [Lines 352–354](/Users/raeez/mathematics/worktrees/frontier-mine-weil-20260913/research-candidates/weil-native-integration/candidate002/paper.tex:352) require a nonzero unit, making the zero algebra nonunital.
- Lines 1479–1484 explicitly give its unitization the usual normed algebra \(\mathbb C\), before the nonzero left-multiplication proof begins.
- Lines 1517–1523 compute its spectrum in \(\mathbb C\). In every specified ambient algebra, \(\lambda1\) is invertible precisely for \(\lambda\ne0\), so \(\sigma(0)=\{0\}\). The nonempty-spectrum proof at lines 1549–1556 now has the necessary \(1\ne0\) premise.
- Consequently the calculus at \(h=0\) gives \(f(h)=f(0)1\), with norm \(|f(0)|\). It lies in the original zero algebra when \(f(0)=0\); its positive square root and positive/negative parts are zero.
- [Lines 1964–1971](/Users/raeez/mathematics/worktrees/frontier-mine-weil-20260913/research-candidates/weil-native-integration/candidate002/paper.tex:1964), p.26, correctly distinguish masses. On \(\mathbb C\),
  \[
  \omega_m(\bar z z)=m|z|^2.
  \]
  Positivity is equivalent to real \(m\ge0\). At \(m=0\), the entire algebra is null, the GNS space and cyclic vector are zero, and \(e_i=0\) converges to that vector. At \(m>0\), the GNS space is one-dimensional, \(\|\Omega\|^2=m\), and the original zero algebra acts as zero. Hence \([e_i]=0\) does not converge to \(\Omega\). These cases agree with the stated definitions of cyclicity and nondegeneracy.

I found no changed mathematical consumer that silently restores the previous convention. The nonzero convolution and operator algebras retain their previous meanings.

Independent verification established:

- All **371** current freeze rows and the aggregate digest match; all **381** predecessor rows remain unchanged.
- All **292** current build-input originals and preserved copies match, with exact FLS input closure.
- Earlier freeze sets of **57, 71, and 360** records, **197** snapshot original/copy records, and **125** accepted build-input original/copy records also match.
- The reader tar contains exactly the source and approved frozen style. Style SHA `07336dc2503195a619a5b566e8730e891d4c81b2465530873214d7087b83e4b5` matches the authorized template.
- The recorded source delta equals the independently generated diff. **27/29** predecessor proofs are byte-identical; the other two have precisely the declared zero-case and nonzero-premise additions. All **15** accepted imported proofs and recorded line/hash correspondences match.
- Exact SymPy calculations independently checked rank-one adjoints/products, evaluation surjectivity, GNS pairing, null-kernel left invariance, and intertwining. A complex \(3\times3\) test gave evaluation rank \(3\), nullity \(6\), and matching positive-square values \(29/3\). These finite checks support the identities, not the infinite-domain conclusion.

All **111** source labels are unique and have actual PDF destinations and matching visible numbers. The recorded **52-label** gate passes. The exception is [paper.aux:66](/Users/raeez/mathematics/worktrees/frontier-mine-weil-20260913/research-candidates/weil-native-integration/candidate002/build/paper.aux:66):
```tex
\newlabel{lem:heights}{{6.1}{9}{Admissible rectangle heights}{lemma.48}{}}
```
The destination and visible Lemma 6.1 are on page **10**. Native001 has the identical discrepancy, and pages 9–10 are byte-identical between versions. No `\pageref` appears in the manuscript; the existing reference uses the correct number and destination. This is a pre-existing auxiliary-page defect, not a failure of either mathematical repair. Moving that label into the lemma’s first sentence would require a new freeze and proportional review.

I visually inspected all **16 changed pages**, all **17 affected adjacent transitions**, and the additional pages 9–10. No clipping, overlap, incorrect visible references, or manuscript-firewall violation appeared. Source, extracted PDF text, and metadata scans were clean. The existing log has no undefined references, duplicate labels, missing destinations, or box warnings; its sole warning concerns disabled shell escape. Reviewed PDF: :codex-file-citation{path="/Users/raeez/mathematics/worktrees/frontier-mine-weil-20260913/research-candidates/weil-native-integration/candidate002/out/paper.pdf" purpose="source"}.

No files changed. No builds, renders, cache writes, Git mutations, or delegation occurred. Checks used Python 3.14.6, SymPy 1.14.0, pypdf 6.14.2, and PyMuPDF 1.27.2. Current backend model/effort metadata remain locally unverified; no mismatch was observed.

This verdict accepts only the mathematical delta and its stated preservation checks. It does not establish RH, global arithmetic positivity, boundary integration, or whole-manuscript acceptance.
