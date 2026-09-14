# Weil core integration: frozen construction and evidence

The saved construction is recovered without changing its 26 reader-source assets.
The full text and standalone chapter build reproducibly in the new worktree.
The mathematical comparison is ready for exact-candidate review. Root retains acceptance authority.
This report does not certify the entire inherited book.

## Custody and scope

- Worktree: `/Users/raeez/mathematics/worktrees/frontier-resume-weil-020-20260914`.
- Branch: `intake/resume-weil-020-20260914`.
- Principal base: `cce2bc383bcf2fd930e917a5abb773e0469465cc`.
- Owned source: `research-candidates/weil-core020/`.
- Owned evidence: `reports/research/CONSTRUCTION-2026-09-14/weil-core020/`.
- Prior source and evidence remain untouched in `frontier-mine-weil-20260913`.
- `custody-import.json` binds 1,960 original/copy pairs, including all prior evidence.
- The full prior report is preserved under `custody019/`.
- The 687 rows of the native018 freeze also match their original files.
- Source closure SHA-256: `bcb9e38729897c25dcbef0ef4361dd01f07eb6aa8f279783b6adbc17b6f147f0`.
- Source aggregate SHA-256: `982d1f489a61b0ab4152e34add7803e1be3066394e0d647560379ebd6a18f903`.
- Weil chapter SHA-256: `aa4e5a679475d0d82c37f75992bc2fef60447bd6d4f83b127f55860656ce66f3`.

The complete required native019, native002 delta, and strict-boundary review inputs were read.
Their assertions were checked against source and preserved evidence within the stated scope.
They do not grant acceptance of this combined candidate.
No September 9 patch or old restoration code was executed.
No source was staged, committed, pushed, or written outside this worktree.
The operational requirement is `gpt-6-astra` with `ultra` effort.
Observed backend model and effort metadata are unavailable here and remain unverified.

## Exact source composition

The full source retains the programme024 core and appends the Weil chapter.
The programme entrypoint adds that chapter and widens the contents number field.
The operator-kernel chapter adds seven lines linking its trace problem to the new comparison.
`core-semantic-integration.diff` records these two inherited-file changes.
No inherited core proof changes.

`proof-correspondence.json` records every native proof and every core proof with source lines and SHA-256 values.
All 33 native proofs survive. Thirty-two are byte-identical.
One has only `_{\rm vM}` changed to `_{\mathrm{vM}}`.
All 138 core proof environments are byte-identical and occur uniquely in their corresponding sources.
The entire native body also matches after three explicit transports:

1. Eight von Mangoldt font subscripts use `\mathrm{vM}`.
2. The nonzero-unit convention is scoped to the chapter's complex involutive algebras.
3. `\Needspace` declarations keep headings with their following text.

The native abstract's mathematical content remains in the chapter opening.
The title and article frontmatter become a chapter heading and mathematical motivation.
Four additional proofs establish the comparison propositions below.
These correspondence checks verify preservation. They are not a fresh acceptance of all inherited theorems.

The source patch contains only the 26 new reader-source paths.
The full reader archive contains exactly those assets.
The standalone reader archive contains its entrypoint, chapter, and approved frozen template.
Operational reports and build products are absent from both reader archives.

## Mathematical comparison

All anchors in this section refer to `manuscript/weil-forms-and-domains.tex` within the owned source.

### Finite trace and the actual formal carrier

Lines 2650–2688 fix the carrier `C[[x,y]]/C` over the discrete complex field.
Its monomials identify it with a countable product of discrete coefficient spaces.
Continuous endomorphisms are exactly row-finite matrices.
The operator topology fixes complete rows in each prescribed finite set of output rows.
This is the topology of the inherited kernel construction, with its field specialized to discrete `C`.

Finite-support matrices form a dense nonunital subalgebra `F_0` of that endomorphism algebra.
The same matrix units act on finite sequences inside the usual Hilbert space `ell^2`.
Conjugate transpose agrees on this subalgebra. No topological identification is claimed.
Finite-support matrices are smaller than the full continuous finite-rank ideal on the formal product.

Proposition 20.19.1, lines 2691–2747, computes

\[
\tau(C^*B)=\sum_{i,j}B_{ij}\overline{C_{ij}},\qquad
\tau(B^*B)=\sum_{i,j}|B_{ij}|^2.
\]

Thus the null space is zero. Coordinate limits and finite truncations prove that the completion is `ell^2(N x N)`.
Left multiplication acts separately on columns. Its norm is at most the Hilbert operator norm of the finite matrix.
A single nonzero finite column gives the reverse inequality.
This proves the exact equality of the two operator norms.

For `Q_n=sum_{i<n} E_ii`, positivity on a unitization of mass `c` would imply

\[
0\leq\tau^+((I-Q_n)^*(I-Q_n))=c-n
\]

for every positive integer `n`. This excludes every finite mass.
The map `(lambda,B) -> lambda I+B` is injective because the infinite identity has infinite support.
It identifies the algebraic unitization with an actual operator subalgebra.
Every linear extension has the displayed form `c lambda+tr(B)` and is cyclic by finite multiplication.
Its restriction is exactly the restriction of the inherited trace `c chi(P)+tr(F)` when `P=lambda I`.
Consequently that inherited trace cannot be positive for any involution extending the finite-matrix involution.
No involution on the larger differential-operator algebra is presumed to exist.

Proposition 20.19.2, lines 2774–2797, uses `T_n=sum_{i<=n} E_i0`.
These matrices converge by rows to `T(h)=h_0(1,1,...)`.
Their transposes have a nonstabilizing zeroth row, so they do not converge in the same topology.
A continuous extension of conjugate transpose would preserve this convergent sequence, which is impossible.
Also, `T(e_0)` is not square-summable. The same coefficient action cannot extend to every formal endomorphism on `ell^2`.
Finally, `E_nn` tends formally to zero while both its Hilbert operator norm and its GNS vector norm equal one.
These examples distinguish formal, operator-norm, and GNS completions.

### Formal coefficients and numerical Gaussian averages

Proposition 20.20.1, lines 2825–2881, fixes the pointwise polynomial algebra with involution fixing its real variable.
For real `h>0`, Gaussian integration by parts gives

\[
\mathbb E_h(u^{2m})=\frac{(2m)!}{2^m m!}h^m,
\qquad \mathbb E_h(u^{2m+1})=0.
\]

Gaussian decay makes all boundary terms zero. Every polynomial integral is absolutely convergent.
The integral of `|p|^2` proves positivity, and polynomial expansion proves the finite derivative formula.

For the formal carrier `C[u][[hbar]]`, the coefficient of `hbar^N` uses only pairs `j+m=N`.
There are finitely many pairs. This defines the map without analytic convergence.
Finite reindexing proves `C[[hbar]]`-linearity, and preservation of every adic power proves continuity.
On `C[u,hbar]`, both specializations involve finite sums and therefore agree.

For nonzero `h`, the element `1-hbar/h` is a unit in `C[[hbar]]`.
A unital complex-algebra homomorphism sending `hbar` to `h` would send that unit to zero.
This proves the obstruction algebraically, without a continuity assumption.
Evaluation at zero remains available.
No positive numerical specialization of every formal series is asserted.

The proposed Gaussian insertion into the Weil algebra also fails at its actual operations:

\[
J_a(1)\star J_a(1)=g_{2a}\ne g_a,
\qquad J_a(u)^*=-J_a(u)\ne J_a(u^*).
\]

It is neither multiplicative nor compatible with the involution.
The positive polynomial average therefore does not transfer through this map.

### Arithmetic positivity and nonunital observables

Lines 2912–2927 construct the formal Hamiltonian action itself.
The bracket is `f_x g_y-f_y g_x` modulo constants, and `a_f=-f_y partial_x+f_x partial_y`.
Output through degree `N` uses only input monomials through degree `N+1` in each nonconstant input.
Thus the action and its map into the row topology are continuous.
The displayed derivative calculation proves `[a_f,a_g]=a_[f,g]`.
This formal action supplies no Hilbert adjoint or numerical specialization by itself.

The inherited local-term calculation at lines 2370–2431 gives

\[
L_\zeta(g_a)=\frac{a^{-1/2}\log(1/a)}{4\sqrt\pi}+O(a^{-1/2}),
\qquad
\frac{|L_\zeta(g_a)|^2}{L_\zeta(g_{2a})}
\sim\frac{\sqrt2}{4\sqrt\pi}a^{-1/2}\log(1/a).
\]

The polar term stays bounded. The prime term has an explicit exponentially small bound.
The gamma term supplies the displayed positive leading coefficient.
The denominator is therefore positive for sufficiently small `a`.

Proposition 20.21.1, lines 2942–2970, excludes a positive functional on any unital complex involutive target algebra.
An alleged factorization extends along `T^+(f+lambda 1)=T(f)+lambda 1_B`.
This is a unital homomorphism preserving the involution.
Composing with the target functional gives a positive unitization of mass `omega(1)`.
The preceding divergent ratio contradicts the finite Cauchy–Schwarz bound.
The argument needs no topology on the map or functional.

A remaining comparison must use a proper nonunital algebra, or a separately defined positive weight with its finite test ideal.
The finite-matrix example establishes that this type of carrier is possible.
It does not construct the arithmetic map or establish `L_zeta=omega o T`.
Under such a factorization, the GNS isometry maps onto the closed subspace `K=closure([T(A_zeta)])`.
The exact graph-domain comparison takes closures in `K` on the restricted domain `E=[T(A_zeta)]`.
Equality with the full target graph domain requires another hypothesis, such as surjectivity.
The native counterexample to ambient-domain equality remains intact.

## Preserved theorem boundary

The test algebra remains the union of weighted smooth convolution algebras with weight exponent greater than one-half.
The Fourier phase is positive, the Mellin coordinate is centered at one-half, and the involution includes reflection.
The strict boundary argument gives `0<Re(rho)<1`. It does not give the critical line or positivity.
Its exponent is `4m-3>=1`, and the second shifted factor only needs boundedness.
The completed multiplier is a holomorphic unit on the open strip, preserving zero orders.

The strict-strip classification agrees with [DLMF 25.10(i)](https://dlmf.nist.gov/25.10#i).
The completion normalization agrees with [DLMF 25.4.3–25.4.4](https://dlmf.nist.gov/25.4#E3).
These official references were checked on 2026-09-14. The local proofs carry the argument.

The GNS derivative example retains exactly `C_c^infinity(0,infinity)` as its represented domain.
Its closure has deficiency dimensions one and zero. No full-adjoint-domain equality is introduced.
The zero algebra remains nonunital under the explicit nonzero-unit convention.
Its unitization, spectrum, zero-mass case, and positive-mass case remain unchanged.

The common graph-domain proof still uses `c=sum a^*a` to control every finite family of graph seminorms.
It uses nets for the full locally convex completion and states that the resulting invariant restrictions need not be self-adjoint.
None of the new comparisons converts a formal character into an operator, cyclicity into positivity, or boundary nonvanishing into RH.

## Verification and rendering

`build.py` gives the exact command, output directory, fixed timestamp environment, return codes, and log hashes.
Each of the full, standalone, and unchanged baseline targets completed two converged `latexmk` runs.
The builds contain no fatal errors, unresolved references, duplicate-label warnings, or box warnings.
Their sole warning records disabled shell escape.
Every font is embedded, subsetted, and Unicode-mapped.

| Target | Pages | PDF SHA-256 |
| --- | ---: | --- |
| Full text | 356 | `ebb2414deec01287094de300cd85f1ef959baba82b59808d9915ee143bd5c0bc` |
| Standalone chapter | 37 | `d810a0a97435a76936c5e086e17fa44a148ba0fd1696f570a51c3b120c650ef9` |
| Unchanged baseline | 320 | `01f6ff1e9ad827370511d7ddbbff45a42ff939f040832093bbfa5a34eabe2e46` |

All 356 full-text page rasters and all 37 standalone page rasters equal the saved construction's rasters.
The fresh baseline reproduces all 320 original baseline page rasters.
Among those 320 pages, 313 remain identical in the integrated text.
The seven changed inherited pages are contents pages 10–15 and the operator-chapter conclusion on page 263.
The new chapter occupies pages 321–356.

All 48 affected full-text pages and transitions were visually inspected.
All 37 standalone pages and all 36 adjacent transitions were visually inspected.
No clipping, overlap, missing glyph, detached heading, or manuscript-firewall violation appeared in these pages.
The 15 contact sheets retain the visual inspection set. The source PNGs remain available at full resolution.
Source, extracted text, metadata, and reader-archive scans keep operational material outside the manuscripts.

All 799 source labels are unique, all references resolve, and all 799 PDF destinations exist.
The 127 Weil labels have correct actual destinations, visible numbers, and physical page values in both PDFs.
All 73 Weil equation labels have exact display-plus-reference occurrence counts.

The expanded whole-book navigation check found 53 discrepancies between recorded AUX pages and actual destinations.
Every discrepancy is an identical record in the fresh unchanged baseline.
None belongs to the Weil chapter. `all-label-destinations.json` records their exact source lines and both page values.
These inherited navigation defects prevent a clean whole-book navigation verdict.
They were preserved and reported without changing inherited proof bytes.

The fresh FLS closures contain 342 full-text inputs, 301 standalone inputs, and 341 baseline inputs.
Every input has a SHA-256 value and a preserved content-addressed copy, including the generated auxiliary inputs.
The entire old evidence custody is separately frozen.

`independent_calculations.py` recomputes 256 matrix-unit product identities, 16 adjoint identities,
the symbolic trace square, operator-norm equality in a nonnormal example, and eight corner projections.
It checks Gaussian moments through degree ten, a formal module-linearity example, and the truncated unit inverse.
It also checks 392 Hamiltonian coefficient identities and the decisive inherited signs and constants.
These calculations use exact SymPy arithmetic. Their finite scope is explicit.
The general arguments are the source proofs described above.
The retained prior calculation script was adapted and rerun separately.

The first verification attempt used `/usr/bin/python3`, which lacks PyMuPDF.
It failed before running any verification.
The successful checks use `/opt/homebrew/opt/python@3.14/bin/python3.14`, with the required libraries already installed.
No failed check is counted as a pass.

## Reproduction and residual obligations

From this worktree, use the report directory `reports/research/CONSTRUCTION-2026-09-14/weil-core020`.
Run `build.py full`, `build.py standalone`, and `build.py baseline` with Python.
Then use the stated Python 3.14 binary for `verify.py`, `inspect_carriers.py`, `all_labels.py`,
`independent_calculations.py`, `exact_checks.py`, and `compare_and_render.py`.
Rebuilding creates new evidence and must be followed by a new freeze before another whole-candidate verdict.

Remaining obligations are explicit:

1. Root must reconcile fresh mathematical and integration reviews against `freeze.json`.
2. The 53 inherited core navigation discrepancies need their own scoped repair and review.
3. Integration into a newer programme core requires a semantic composition and a new candidate review.
4. Independent arithmetic positivity, RH, the positive current-observable comparison, and determinant multiplicities remain unresolved.
5. No whole-book acceptance, central accepted-PDF replacement, commit, push, or publication occurred.

No mathematical defect was found in the four comparison proofs or their declared source transport.
This construction supplies exact obstructions and conditional comparisons, with the arithmetic existence problem still open.
