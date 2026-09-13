CR-G08-P004 is complete as a bounded reading investigation. Both assigned text occurrences, their required opening and adjacent context, and the entire packet were read. Mathematical acceptance is **not** granted.

The main findings are:

- The recovered §13.3 overstates the range of its GNS embedding. Its Hilbert–Schmidt completion remains correct after a small proof repair.
- The live manuscript’s proposed Bost–Connes state contradicts the isometry relation. Its subsequent GNS identification therefore fails as written.
- The live modular operator and half-density formulas have the wrong sign for the stated KMS convention.
- The recovered analytic, finite arithmetic, and finite-prime Hochschild constructions largely survive on their specified carriers. They do not establish integral field descent, ramified chiral realization, or the full global center.

**Custody and controls**

```yaml
assignment_id: CR-G08-P004
wrapper_sha256: 9efdfde0e444831040c8f5d55bcdf4e9f07809931dadf53d6425ccd8e5f0a562
group_sha256: 8df9d17703a3e53db8bddf41d6c03b8dbcfda0d252892fe8b3a2360c614a7103
reader_contract_sha256: 4c9cd2fcda6930663e88433a090cc3199cb8a8b406ce246dc83851ece0d0b927
inventory_sha256: 170a2ffef4ece931149e75ef36eafee3f0cfc2331fcd406da987e7a4897eb1b5
live_routing_sha256: 9538467b5fc11a50da5be5bdda03f459daa7a14cccee8adfe530654c800e9f48
registry_sha256: 9aaad3b74f75b188361a81772e1f378c0603aee94b69657ba27aa4c4e185aefb
packet_id: 085--programme--ledger--0e5599715717ec30
packet_sha256: 15a5f438e2a2810b3424d4d040b6f47514c074dae2fda3bfb577d2e65201c0ac
packet_bytes_read: [0, 75448]
non_target_units: []
requested_model: gpt-6-astra
requested_effort: ultra
observed_model: unverified
observed_effort: unverified
observed_control_mismatch: none_observed
independence: No sibling proposals or verdicts received before these derivations.
live_repository: /Users/raeez/chiral-bar-cobar-vol4
live_commit: 10157885d7d9df587df8bf43804acabcbb7ad850
live_status: clean at initial and final checks
changed_paths: []
staged_paths: []
descendants: []
```

The complete assignment object was exposed in sequential, nontruncated chunks. All 64 occurrence hashes and all 90 supplied opening, adjacent-context, and heading hashes matched. The relevant inventory occurrences match the assignment exactly, with the additional inventory field `owner_assignment_id: CR-G08-P004`. Unrelated inventory pages and occurrences were not given reading credit.

The assignment’s broad question mentions integral fields and ramification, but its frozen bytes principally cover Chapters 12–16 and the beginning of Chapter 17. The remainder of §§17.2–17.3 was read as required adjacent context. The later integral-field chapters are separately owned; the title of the assignment does not supply their proofs.

**Document and visual ledger**

Let **D6** denote the extracted document with SHA-256  
`dca11a76bf0c95aa721c039cd7cf71fb363f9f09b43d33317dc29bce554306fe`, and **D5** the document with SHA-256  
`82a386fffa303b71780b15490092365734bc31b8bc5e2b976503b23331af8cb1`.

Their source PDFs are:

- Integral v6: SHA-256 `1be99da95e6c684fe2a730bd4981b8bf824ffe280cfb8efb9b88c9e0e30c3c34`.
- Construction v5: SHA-256 `b04ff4ed9d62c17f0c47501767b8576df366a8eb4f4279538bdd1a8adc78252e`.

All byte intervals below are half-open.

| Document | Exact interval read | Role | Interval SHA-256 |
|---|---:|---|---|
| D6 | `[0,9938)` | Required opening | `3a1b6a47f60bb7de756602f7bb36441932f2b5e62aed88e8ddc0e9ff2043baa0` |
| D6 | `[198506,268580)` | Assigned occurrences | `9f819e490f9cd7026d2ea7aba0d1591cc8dedd7794a828008c5c82903781ef3d` |
| D6 | `[196613,273758)` | Required adjacent context, including assigned interval | `d324fa5d375c37c806687ee7936969462ed7f4e4e9f97a910d2366c610e60e65` |
| D5 | `[0,8762)` | Required opening | `af320f1afa9fde61c34c9308c61252eb1ea692eb6b8e3823b7368458a5c3ed55` |
| D5 | `[192803,262877)` | Assigned occurrences | `9f819e490f9cd7026d2ea7aba0d1591cc8dedd7794a828008c5c82903781ef3d` |
| D5 | `[190910,268055)` | Required adjacent context, including assigned interval | `d324fa5d375c37c806687ee7936969462ed7f4e4e9f97a910d2366c610e60e65` |
| D6 | `[71440,90079)` | Chapter 3, lines 1088–1414; definitions and bar comparison | `30a93a4423e93ba2ed963e0381aeddad4675f0f674c89994763bb2b4eb60d15d` |
| D6 | `[185274,190730)` | Lines 3080–3182; adjacent arithmetic and gamma conventions | `44f3be7f49cadb35ea46a5a3b0483c39c3011e2913ff156d4a8fbfe5d22e0b51` |
| D6 | `[918774,923274)` | Bibliography, lines 15485–15565 | `db9b20d25bbf72e00a99818e867549634504cff7a07d4ed89960409e941e61d7` |

Physical PDF pages visually inspected:

```yaml
Integral_v6: [5, 84, 86, 87, 89, 90, 92, 98, 99, 105, 106]
Construction_v5: [4, 82, 84, 85, 88, 90, 97, 103, 104]
unread_required_text_intervals: []
full_parent_reading_claim: false
```

The PDF checks confirmed the conjugations in \(f^*(u)=\overline{f(-u)}\), \(h(z)=\overline{F(\bar z)}F(z)\), and Gaussian interpolation. They also confirmed the recovered GNS overstatement, the cyclic-cocycle formula, and the diagonal differential signs. Other physical pages were not visually inspected; text reading must not be reported as whole-PDF visual review.

Images were rendered directly to process output and displayed from memory, without creating files. No build, test suite, restoration script, or archived executable was run.

**Claim records**

The following records apply separately to both occurrences listed in the unit ledger below. “Survives” means the stated argument was reconstructed under the indicated hypotheses; it does not constitute programme acceptance. Unless a live anchor is supplied, exact live theorem correspondence remains unresolved.

**C01 — Poisson summation, §12.1.**  
For every complex Schwartz function \(f\) on \(\mathbb R\), with \(\widehat f(\xi)=\int f(x)e^{-2\pi ix\xi}\,dx\), the two absolutely convergent sums \(\sum_n f(n)\) and \(\sum_m\widehat f(m)\) agree. Periodization and integration by parts give the stated uniformly convergent Fourier series. The Gaussian is the first deciding example. This scalar result survives; it constructs no arithmetic collision operation. Confidence: high.

**C02 — Gaussian transform and theta reflection, §12.1, (12.1).**  
For \(t>0\), \(\widehat{e^{-\pi tx^2}}(\xi)=t^{-1/2}e^{-\pi\xi^2/t}\), hence \(\vartheta(t)=t^{-1/2}\vartheta(1/t)\). Differentiation under the integral gives the linear ODE and the Gaussian integral fixes the normalization. This survives over the real/complex analytic carrier. It is not a statement over arbitrary coefficient fields. Confidence: high.

**C03 — Completed scalar functional equation, §12.2, Theorem 12.1.**  
With \(\Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2)\), the split theta integral gives
\[
\Lambda(s)=\frac1{s-1}-\frac1s+
\frac12\int_1^\infty(\vartheta(t)-1)
\bigl(t^{s/2-1}+t^{(1-s)/2-1}\bigr)\,dt.
\]
The integral is entire, the residues are \(-1,1\) at \(0,1\), and \(\xi(s)=s(s-1)\Lambda(s)/2\) is entire with \(\xi(0)=\xi(1)=1/2\). The local uniform exponential majorant proves the continuation. The failed stronger route is continuation of the occupation heat operator as trace class: its diagonal singular values are \(n^{-\Re s}\), whose sum diverges for \(\Re s\le1\). Scalar continuation survives; operator continuation does not follow. Confidence: high.

**C04 — Euler product and logarithmic derivative, §12.3.**  
For \(\Re s>1\),
\[
\zeta(s)=\prod_p(1-p^{-s})^{-1},\qquad
-\zeta'(s)/\zeta(s)=\sum_{p,r\ge1}(\log p)p^{-rs}.
\]
Finite products enumerate supported integers; absolute summability justifies the limit and differentiation. The deciding distinction is multiplicative enumeration versus the additive Fourier identity used in C03. Neither proves a chiral coproduct/collision comparison. Confidence: high.

**C05 — Operator Euler product, §12.4, Theorem 12.2.**  
On \(L^2(\mathbb R_{>0},x^{2\sigma}dx/x)\), \(\sigma>1\), \(D_nf(x)=f(nx)\) has norm \(n^{-\sigma}\). The series \(\sum D_n\) and \(\sum\mu(n)D_n\) converge in operator norm and multiply to \(I\). The coefficient at \(D_n\) is \(\sum_{d\mid n}\mu(d)\). The same summable majorant proves both prime products. The construction survives for unital bounded monoid representations with the stated norm bound. No continuation outside that norm domain was established. Confidence: high.

**C06 — Mellin intertwining and quantum obstruction, §12.4.**  
On smooth compactly supported functions, \(M(D_nf)(s)=n^{-s}Mf(s)\) and \(M(-x\partial_xf)(s)=sMf(s)\). Substitution and integration by parts prove both. Commuting dilations cannot faithfully retain \(x_jx_i=q_{ij}x_ix_j\) when a nontrivial \(q_{ij}\) acts as a scalar and \(x_ix_j\) has nonzero image. The strongest construction is the untwisted monoid representation, with a separate domain for the unbounded generator. Confidence: high.

**C07 — Existing nuclear spectral realization, §12.5, Classical input 12.3.**  
Meyer’s quotient \(H_-^0=H_-/ZH_\cap\) and its scaling representation supply a nuclear character realization. The transpose generator has the zeta zeros with their algebraic multiplicities. This was checked against Theorem 3.3, Theorem 4.1, Corollary 4.2, and Theorem 5.8, printed pp. 6–8 and 12. It does not establish the programme’s positive Hilbert or chiral comparison. The surviving construction is the named nuclear quotient; the residual is an actual comparison map preserving traces and the additional positivity/domain structures. Confidence: high on source correspondence. [Meyer, arXiv:math/0412277v3](https://arxiv.org/pdf/math/0412277)

**C08 — One-prime KMS state, §13.1, Theorem 13.1.**  
For the Toeplitz algebra generated by \(Se_r=e_{r+1}\), \(\alpha_t(S)=p^{it}S\), and every \(\beta>0\),
\[
\phi_{\beta,p}(a)=(1-p^{-\beta})\operatorname{Tr}(p^{-\beta N}a),
\quad
\phi_{\beta,p}(S^mS^{*n})=\delta_{mn}p^{-m\beta}.
\]
Invariance kills nonzero frequencies, and KMS determines the diagonal moments. The geometric density supplies existence. In particular \(\phi(S^*S)=1\) while \(\phi(SS^*)=p^{-\beta}\). This deciding identity survives and exposes live defect L01 below. Confidence: high.

**C09 — Infinite prime product and normality threshold, §13.2, Theorem 13.2.**  
The unital inductive limit of finite minimal tensor products has one KMS state for each \(\beta>0\). Unique factorization makes every zero-frequency monomial diagonal in its prime exponents. For \(\beta>1\), its occupation realization has density \(\zeta(\beta)^{-1}e^{-\beta H}\). For \(0<\beta\le1\), finite-prime vacuum projections decrease to rank-one projections whose forced state values vanish. Normality would then contradict \(\sum_nP_n=I\) strongly. The \(C^*\)-state survives below the threshold; a normal density in this representation does not. Confidence: high.

**C10 — GNS range overstatement, §13.3. VERIFIED DEFECT, severity 3.**  
Exact attacked sentence: “All finite-rank operators lie in its range after rescaling matrix units.” D6 byte `213440`, line `3579`; D5 byte `207737`, line `3488`; printed p. 67 in both editions, physically v6 p. 84/v5 p. 82.

Let \(\rho_n=\zeta(\beta)^{-1}n^{-\beta}\), \(\beta>1\), and
\[
v_n=n^{-(\beta+1)/2},\qquad T=|e_1\rangle\langle v|.
\]
Then \(v\in\ell^2\), so \(T\) has rank one. If \(T=a\rho^{1/2}\) for bounded \(a\), taking adjoints and applying to \(e_1\) would give \(v=\rho^{1/2}a^*e_1\). But \(\rho^{-1/2}v\) has coordinates proportional to \(n^{-1/2}\), which are not square summable. Thus \(T\) is outside the range.

The failed route confuses finite rank with finite matrix support. Every matrix unit \(E_{mn}\), and hence every finite-support matrix, does lie in the range. Their span is Hilbert–Schmidt dense, which proves the claimed completion. Minimal repair: replace the false range assertion by this density proof. Confidence: high. Exact live sentence not located.

**C11 — Modular Hilbert–Schmidt model, §13.3.**  
After C10’s repair, the completion is \(HS(\mathcal H)\), with left multiplication,
\[
J\xi=\xi^*,\qquad
\Delta E_{mn}=(n/m)^\beta E_{mn},\qquad
\sigma_t^\phi(a)=\rho^{it}a\rho^{-it}=\alpha_{-\beta t}(a).
\]
The operator \(\Delta\) has the maximal diagonal domain
\(\sum_{m,n}(n/m)^{2\beta}|\xi_{mn}|^2<\infty\). Finite matrix truncations form a graph core. The distinction \(J(a\rho^{1/2})=\rho^{1/2}a^*\), rather than \(a^*\rho^{1/2}\), is correct. The two-level nontracial density already decides the sign. This survives and contradicts live L03. Confidence: high.

**C12 — Arithmetic diagonal and distinct Gibbs states, §13.4.**  
The displayed root-of-unity relations hold in the standard representation on \(\ell^2(\mathbb N)\). The finite root sum gives the divisibility projection. At \(\beta>1\), conjugate embeddings give opposite nonzero imaginary expectations at \(r=1/3\), while their restrictions to the prime Toeplitz algebra coincide. Thus a common partition function does not identify the algebras or states. The presentation and representations were checked against Bost–Connes Proposition 18, Propositions 23–24, and Theorem 25, printed pp. 21–22, 31–33. Confidence: high. [Bost–Connes, IHES/M/95/38](https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/CONNES/1994-1998/M_95_38/M_95_38_web.pdf)

**C13 — Nonunital GNS and boundedness, §13.5.**  
For a positive functional on a complex \(*\)-algebra, polarization yields Cauchy–Schwarz on products. Its null space is a left ideal because applying that inequality to \(b\) and \(a^*ab\) forces \(W(b^*a^*ab)=0\) when \(W(b^*b)=0\). The quotient gives a densely defined \(*\)-representation; \(\pi(a^*)\subseteq\pi(a)^*\), so \(\pi(a)\) is closable. Boundedness is equivalent to
\(W(b^*a^*ab)\le C_a^2W(b^*b)\) for all \(b\). No automatic essential self-adjointness follows. The argument survives. Confidence: high.

**C14 — Unitization and positivity factorization, §13.5.**  
On finitely supported sequences with pointwise multiplication, \(W(a)=\sum_nna_n\) is positive. An extension of mass \(M<\infty\) to the unitization would require \(M\ge W(e_n)=n\) for every coordinate projection, an impossibility. Also \(W=\omega\circ T\) with \(T\) a \(*\)-homomorphism and \(\omega\) positive implies positivity, but existence without an independently constructed \(T,\omega\) merely restates positivity through the identity factorization. Both obstructions survive. Residual: construct the comparison functional, rather than assume its factorization. Confidence: high.

**C15 — Analytic test algebra and involution, §14.1, Definition 14.1.**  
The union of smooth functions with all exponentially weighted derivative moments finite for some \(a>1/2\) is closed under convolution and \(f^*(u)=\overline{f(-u)}\). Its transform \(F(z)=\int f(u)e^{izu}du\) is holomorphic in \(|\Im z|<a\) and rapidly decreasing on smaller closed strips. For \(g=f^**f\),
\(h(z)=\overline{F(\bar z)}F(z)\). This follows directly by substitution and Fubini; the PDF confirms both conjugations. The failed extraction-based attack would replace this by \(F(z)^2\) or \(|F(z)|^2\) at nonreal \(z\). Confidence: high.

**C16 — Zero growth, reciprocal-square summability, and horizontal contours, §14.2.**  
The theta formula bounds \(\log\max_{|s|\le R}|\xi(s)|\) by \(O(R\log(R+2))\). Jensen gives the same zero-count bound; the Euler product and reflection confine zeros to the closed critical strip. Dyadic summation gives \(\sum_\rho|\rho|^{-2}<\infty\). Hadamard then supplies
\(\xi'/\xi=B+\sum_\rho(1/(s-\rho)+1/\rho)\).
Excluding intervals of radius \(j^{-2}\) around zero heights in \([j,j+1]\) leaves admissible heights because the total excluded length is \(O(\log j/j)\). The resulting polynomial bound kills horizontal contour terms against rapid decay.

The derivation survives conditional on the named Jensen and Hadamard theorems. Their exact primary-source locators were not independently retrieved in this investigation; that citation gate remains open. Confidence: high on the estimate, with that source-verification limit.

**C17 — Explicit formula, §14.3, Theorem 14.4.**  
On C15’s algebra, the recovered formula is
\[
\sum_\rho h(-i(\rho-\tfrac12))
=h(i/2)+h(-i/2)+\frac1{2\pi}\int_{\mathbb R}h(t)
\bigl(\Re\psi(\tfrac14+\tfrac{it}2)-\log\pi\bigr)dt
-\sum_{n\ge2}\frac{\Lambda_{\rm vM}(n)}{\sqrt n}
\bigl(g(\log n)+g(-\log n)\bigr).
\]
The contour proof retains the two logarithmic residues \(-1\), uses \(1<c<a+1/2\), and moves the gamma term only across a pole-free region. The prime, zero, and gamma majorants are summable. This survives with C16’s imported complex-analysis inputs. It identifies a scalar distribution, not a native arithmetic complex. Direct retrieval of the original Weil paper was not completed. Confidence: high on the reconstructed normalization.

**C18 — Gaussian detection and Weil positivity criterion, §14.4.**  
For a locally finite conjugation-invariant multiset in a bounded horizontal strip with polynomial counting, positivity of
\[
Q_{\mathcal Z}(F)=\sum_{z\in\mathcal Z}F(z)\overline{F(\bar z)}
\]
for every complex polynomial times a translated Gaussian is equivalent to all points being real. Interpolation assigns values \(1,-1\) at a selected nonreal conjugate pair and zero at all other points in a finite vertical band. The normalized Gaussian fixes those two values, and the remaining tail is \(O(e^{-a\delta})\). Thus the pair contributes \(-2m\), eventually dominating the tail. This is a general proof, not a finite grid check.

Together with C17, the criterion is equivalent to RH. It does not prove its positivity hypothesis. The polynomial degree is allowed to grow with the spectral cluster. Confidence: high.

**C19 — Negative archimedean term and unavailable exact gap, §14.5.**  
For \(k(t)=\Re\psi(1/4+it/2)-\log\pi\), the series proves \(k(0)<0\), evenness, and strict increase for \(t>0\). Gaussian concentration near zero therefore gives a negative isolated gamma quadratic form. The full Weil functional retains its prime and polar terms. A transform holomorphic across the real axis cannot vanish on a real interval unless it is zero, so exact high-frequency support supplies no nonzero test in C15’s algebra. Approximate localization remains meaningful but requires estimates for all terms. Confidence: high.

**C20 — Duality, positivity, and adjoint domains, §14.6.**  
The matrices \(\Theta=\operatorname{diag}(1/2+a,1/2-a)\), \(J=\begin{pmatrix}0&1\\1&0\end{pmatrix}\), \(a\ne0\), satisfy \(\Theta^*J=J(1-\Theta)\) with an indefinite form and off-center spectrum. Conversely the actual Hilbert-space equality \(\Theta^*=1-\Theta\), including domains, makes \(-i(\Theta-1/2)\) self-adjoint. The symmetric operator \(-i\partial_x\) on \(C_c^\infty(0,1)\) has deficiency vectors \(e^{\pm x}\), demonstrating why a formal integration-by-parts identity is insufficient. These deciding examples survive. Residual: positivity and closed adjoint-domain equality for the actual arithmetic operator. Confidence: high.

**C21 — Frobenius orbits and formal Euler products, §15.1.**  
For separated finite-type \(X/\mathbb F_q\), \(N_n=\sum_{d\mid n}dB_d\), and Möbius inversion gives \(B_n=n^{-1}\sum_{d\mid n}\mu(d)N_{n/d}\). Consequently
\(Z_X(T)=\prod_x(1-T^{\deg x})^{-1}
=\exp(\sum N_nT^n/n)\).
The product lies in \(\mathbb Z[[T]]\); logarithms are taken after extension to \(\mathbb Q[[T]]\). The orbit count proves integrality before division. The occupation coalgebra realizes this counting series but does not reconstruct étale cohomology. Confidence: high.

**C22 — Projective-line divisors, §15.2, Proposition 15.1.**  
For \(\mathbb P^1/\mathbb F_q\), \(N_n=q^n+1\), \(Z(T)=((1-T)(1-qT))^{-1}\), and effective degree-\(d\) divisors number \((q^{d+1}-1)/(q-1)\). Factorization of nonzero binary forms modulo scalar gives the bijection. The first six closed-point counts over \(\mathbb F_2\), independently computed, are \(3,1,2,3,6,9\). The symmetric-algebra character agrees, but equality of generating functions does not identify the three underlying objects. Confidence: high.

**C23 — Geometric cohomology carrier, §15.3, Classical input 15.2. HYPOTHESIS GAP, severity 3.**  
The intended statement uses
\[
H^i_{\mathrm{\acute et}}
(X_{\overline{\mathbb F}_q},\mathbb Q_\ell),
\qquad \ell\nmid q,
\]
for a smooth projective geometrically connected curve. The recovered wording says “its etale cohomology” without explicitly naming the geometric base change or coefficient field. Those omissions matter: the arithmetic scheme’s cohomology and arbitrary positive-characteristic coefficients do not have the asserted meaning.

Milne Proposition 14.2, Theorem 24.1, Theorem 27.6, Remark 27.7, and Theorem 27.15 support the geometric carrier, its dimensions \(1,2g,1\), trace formula, duality, and purity. Minimal repair: name this carrier at first use. This is not a refutation of the classical theorem. Confidence: high on the correction. [Milne, Lectures on Étale Cohomology](https://www.jmilne.org/math/CourseNotes/LEC.pdf)

**C24 — Determinants, Jordan information, and supertrace, §15.3, Proposition 15.3.**  
For a finite-dimensional characteristic-zero vector space,
\[
\det(1-TF)=\exp\left(-\sum_{n\ge1}\operatorname{Tr}(F^n)T^n/n\right).
\]
Triangularization proves this without semisimplicity. A scalar matrix and a nontrivial Jordan block with the same diagonal have identical power traces and determinant but are not conjugate. The superalgebra \(\operatorname{Sym}(H^0\oplus H^2)\otimes\Lambda(H^1)\) gives the alternating determinant because an odd generator contributes \(1-\alpha T\).

The characteristic-zero hypothesis is essential to this trace-recovery argument. In characteristic \(p\), \(I_p\) and \(0_p\) have all power traces equal to zero, but determinants \(1-T^p\) and \(1\). No all-field reconstruction follows. Confidence: high.

**C25 — Elliptic finite example, §15.4.**  
For \(E:y^2=x^3-x\) over \(\mathbb F_5\), direct counting gives \(N_1=8\). With C23’s geometric input, \(P_E(T)=1+2T+5T^2\), eigenvalues \(-1\pm2i\), and recurrence \(a_n=-2a_{n-1}-5a_{n-2}\). Hence \(N_2=32\), \(N_3=104\). Independent enumeration of all pairs in \(\mathbb F_5[t]/(t^2-2)\) gave \(32\) points including infinity. This verifies that finite count, not general purity. Confidence: high.

**C26 — Functional equation without purity, §15.5.**  
A nondegenerate alternating form with \(F^TJF=qJ\) gives eigenvalue pairing \(\alpha,q/\alpha\) and determinant \(q^g\), hence the stated reciprocal polynomial identity. The matrix \(F=\operatorname{diag}(\sqrt q\,r,\sqrt q/r)\), \(r>0,\ r\ne1\), preserves the similitude form but violates modulus \(\sqrt q\). Formal duality therefore does not prove purity. The geometric purity input remains indispensable. Confidence: high.

**C27 — Collision and motive comparison, §15.6.**  
Closed-point occupation data retain divisor enumeration while omitting geometric extension across diagonals. Local motive factors require a specified Frobenius module with the relevant inertia/monodromy restrictions. No map from the occupation coalgebra to those objects is constructed here. This is a correctly stated residual, not a nonexistence theorem. Next construction: define the geometric factorization object and comparison maps, retaining cohomological degree, weight, occupation, and energy separately. Confidence: high on the scope boundary.

**C28 — Cyclic associator, §16.1, Proposition 16.1.**  
For \(C_m\), \(m\ge1\), the carry function satisfies (16.1). The coboundary exponent of \(\omega_k(a,b,c)=\exp(2\pi ik\,a\,c(b,c)/m)\) is \(m\,c(a,b)c(c,d)\); hence the exponential is one. Normalization gives the unit constraints. This constructs the stated monoidal category over \(\mathbb C\), or an explicitly chosen coefficient ring containing the required unit-valued cocycle. It supplies neither braiding nor arithmetic realization. Exact checks for \(m=1,\dots,8\) found no failures among 8,772 quadruples; the carry identity is the general proof. Confidence: high.

**C29 — Real-place coefficient obstruction, §16.2, Proposition 16.2.**  
The alternating resolution with maps \(1-g,1+g\) gives \(H^n(C_2,\mathbb F_2)\cong\mathbb F_2\) for every \(n\ge0\). For modules over rings in which \(2\) is invertible, averaging makes invariants exact and positive-degree cohomology vanishes. Thus a uniform arithmetic duality assertion cannot ignore coefficient characteristic at real places. This obstruction survives; real-place modification must be specified in a broader theory. Confidence: high.

**C30 — Closed arithmetic CS action, §16.3, Classical input 16.3.**  
For totally imaginary \(F\), \(X=\operatorname{Spec}\mathcal O_F\), a chosen roots-of-unity coefficient identification, finite \(G\), \(c\in H^3(G,\mathbb Z/m)\), and continuous \(\rho:\pi_1(X)\to G\), the invariant map gives \(\mathrm{CS}_c([\rho])=\operatorname{inv}(\rho^*c)\). Conjugation independence follows from the inner-automorphism homotopy; cocycle changes give coboundaries. Kim’s version 4, §1, printed pp. 1–3, matches these hypotheses. No arbitrary number-field, coefficient, open-boundary, or infinite-gauge extension follows. Confidence: high on the imported statement and formal invariance. [Kim, Arithmetic Chern–Simons Theory I](https://arxiv.org/pdf/1510.05818)

**C31 — Primitive torsors, §16.4.**  
For an exact \(z\in Z^3(C)\), \(T_z=\{b\in C^2:db=z\}/dC^1\) is an \(H^2(C)\)-torsor. Difference of primitives proves freeness and transitivity. Exactness is necessary: taking \(C^2=0,C^3=\mathbb Z,z=1\) makes the proposed torsor empty. The pushout through \(\ell:\prod_vH^2(C_v)\to\mathbb R/\mathbb Z\) is a torsor under the target group, without requiring \(\ell\) to be injective or surjective. This survives. Confidence: high.

**C32 — Reciprocity and primitive independence, §16.4, Proposition 16.4.**  
Assume a global primitive exists and \(\ell\) kills the image of global \(H^2\). Two choices differ by a global closed cochain, so their local difference has zero displacement in the pushed-out torsor. This proves choice independence. It does not prove vanishing of the raw tuple of local classes. Functoriality under conjugation additionally needs coherent cochain homotopies; Kim §2, printed pp. 4–6, explicitly constructs them. The elementary torsor statement survives with its assumptions. Confidence: high.

**C33 — Finite groupoid sums, §16.5.**  
For finitely many isomorphism classes, finite automorphism groups, and complex invariant weights,
\(Z=\sum_{[x]}w(x)/|\operatorname{Aut}(x)|\).
For \(S/G\), orbit–stabilizer gives \(Z=|G|^{-1}\sum_{s\in S}w(s)\). Two objects with weights \(1,-1\) already give \(Z=0\), so normalized expectations require \(Z\ne0\). Arithmetic finiteness is an additional input. These formulas cannot be reduced to fields in which the automorphism denominators are nonunits without a different construction. Confidence: high.

**C34 — Wilson maps, averages, and Euler factors, §16.6.**  
The well-typed observable is \(\operatorname{Tr}(R(\sigma(\operatorname{Frob}_p)))\), with \(R:G\to GL(V)\), \(\sigma:\pi\to G\), and an unramified conjugacy class. A homomorphism from a local Galois group is not \(R\). A two-field average of sign values \(1,-1\) is zero, not either selected value. A first trace does not determine a determinant: \(I_2\) and \(\operatorname{diag}(0,2)\) decide the stated endomorphism claim. An invertible variant is \(I_2\) versus \(\operatorname{diag}(1/2,3/2)\). Characteristic-polynomial data, or enough power traces with the coefficient hypotheses, are required. Confidence: high.

**C35 — Profinite and physical passage, §16.7.**  
The finite cocycle, arithmetic action, torsor, and groupoid sum do not themselves define a profinite limit, continuous gauge integral, bordism functor, or determinant realization of \(\xi\). Compatible transitions and measures must be constructed. This is an unresolved construction boundary, not a proof that such a theory is impossible. Next deciding check: a specified inverse system with a proved summation/trace compatibility theorem. Confidence: high.

**C36 — Three endomorphism objects, §17.1.**  
The vacuum object \(R\operatorname{Hom}_A(R,R)\), diagonal object \(R\operatorname{Hom}_{A^e}(A,A)\), and strict graded center differ. For one degree-one exterior generator, the vacuum model is \(R[[x]]\), whereas the cup model is \(\Lambda_R(e)[[x]]\) with zero differential. This already separates them. The finite-prime algebra here is \(R\)-free; an arbitrary nonflat dg algebra requires care about the derived enveloping algebra and relative versus absolute Hochschild theory. No native mixed Deligne comparison is proved by this distinction. Confidence: high for the finite-free family.

**C37 — Diagonal resolution, §17.2, Lemma 17.1 and Theorem 17.2; partly adjacent context owned by P005.**  
For finite prime labels, commutative \(R\), and units \(q_{ij}\), Chapter 3 defines the free quantum exterior algebra, conilpotent coalgebra \(C_q\), and degree-one twist. The displayed differential on \(A\otimes C\otimes A\) squares to zero: pure terms use \(\tau\star\tau=0\), and mixed terms cancel by the degree-one sign and coassociativity. Augmentation cancels the two endpoint terms.

The comparison with the two-sided bar is a quasi-isomorphism using the occupation-preserving coalgebra map \(j\). For each total occupation, the outer-length filtration is finite; there is no hidden infinite convergence argument. The diagonal’s two cut terms cancel after balancing over \(A\). The construction survives in this finite-free setting. Confidence: high. No independent completion credit for P005 is claimed.

**C38 — Completed cup model, §17.3, adjacent context owned by P005.**  
Evaluation on \(1\otimes C\otimes1\) gives
\[
\operatorname{Hom}_R(C,A),\qquad
df=\tau\star f-(-1)^{|f|}f\star\tau.
\]
The convolution has no coalgebra tensor sign because \(C\) is concentrated in degree zero. Since \(A\) is finite free, the Hom product is \(A_q\otimes_RR_q[[x_1,\ldots,x_d]]\), with \(|x_i|=0\), \(x_jx_i=q_{ij}x_ix_j\), and differential \([\sum e_ix_i,-]\). The quadratic relations cancel its square, including characteristic two because \(e_i^2=0\) is imposed.

The bar comparison preserves diagonals and hence cup products. It does not automatically restrict ordinary braces to the small model. Negron Theorem 1.1/5.3 supports the twisting-cochain cup comparison over a field; the manuscript’s explicit free resolution is needed for its arbitrary-ring extension. Confidence: high on this bounded construction. [Negron, arXiv:1304.0527v4](https://arxiv.org/pdf/1304.0527)

**Live defects and correspondences**

All live records below refer to commit `10157885d7d9df587df8bf43804acabcbb7ad850`.

**L01 — Proposed state does not descend to the algebra. VERIFIED DEFECT, severity 2.**  
[46_KMS_GNS_full_sector.tex](/Users/raeez/chiral-bar-cobar-vol4/chapters/arithmetic/46_KMS_GNS_full_sector.tex:246), lines 246 and 266, states both \(\mu_m^*\mu_m=1\) and
\[
\phi_1(\mu_n^*\mu_m e(\gamma))
=\delta_{nm}m^{-1}\widetilde e_p(\gamma).
\]
Set \(n=m>1,\gamma=0\). This gives \(\phi_1(1)=1/m\), while \(m=n=1,\gamma=0\) gives \(1\). No linear functional on the presented algebra has these values. The GNS-space lemma, modular calculation, and pairing transfer that use this formula are unsupported.

The factor \(m^{-1}\) belongs to the range projection \(\mu_m\mu_m^*\) under KMS\(_1\), not to \(\mu_m^*\mu_m\). Repair requires constructing a consistent state on the full arithmetic algebra and rederiving its GNS space; swapping symbols in one display alone does not certify the downstream theorem. Confidence: high.

**L02 — False covariance used to infer tensor structure. VERIFIED DEFECT, severity 2.**  
The same file, line 335, uses
\(\mu_me(\gamma)\mu_m^*=e(m\gamma)/m\).
At \(\gamma=0\), this asserts that a nonzero range projection equals \(I/m\), which is not idempotent for \(m>1\). The correct relation is the root-of-unity average displayed at lines 247–248. The claimed tensor decomposition cannot be inferred from the false relation. Confidence: high.

**L03 — Modular sign and half-density. VERIFIED DEFECT, severity 2.**  
The same file, lines 362–389 and 403–411, claims \(\Delta\mu_m\Omega=m\mu_m\Omega\) and \(J\mu_m\Omega=m^{-1/2}\mu_m^*\Omega\). Its own proof first states \(\sigma_t^\phi=\sigma_{-\beta t}\), then substitutes \(\beta=1\) to obtain the opposite sign.

For a consistent KMS\(_\beta\) state with the stated evolution,
\[
\|\mu_m\Omega\|^2=1,\quad
\|\mu_m^*\Omega\|^2=m^{-\beta},\quad
\Delta\mu_m\Omega=m^{-\beta}\mu_m\Omega,\quad
J\mu_m\Omega=m^{\beta/2}\mu_m^*\Omega.
\]
The live factor \(m^{-1/2}\) fails the antiunitary norm test. The recovered C11 has the correct time sign. Full repair remains dependent on L01. Confidence: high.

**L04 — Classical source scope mismatch. VERIFIED SOURCE CONFLICT, severity 3.**  
Lines 260–272 cite Bost–Connes Theorem 25 for a prime-local KMS\(_1\) state and type III\(_1\) assertion. The retrieved Theorem 25 explicitly assumes \(\beta>1\) and concerns the global rational system. It cannot justify the quoted prime-local statement. The original paper handles \(0<\beta\le1\) separately in §7. The next step is a correctly scoped prime-local state construction or a precise restriction theorem. Confidence: high. [Bost–Connes, Theorem 25, printed p. 33](https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/CONNES/1994-1998/M_95_38/M_95_38_web.pdf)

**L05 — Live Weil normalization and carrier need reconstruction. UNDECIDED, severity 3.**  
[59_R_analytic_weil_gaussians_formal.tex](/Users/raeez/chiral-bar-cobar-vol4/chapters/arithmetic/59_R_analytic_weil_gaussians_formal.tex:307), lines 307–460, mixes a Fourier convention with \(2\pi\), evaluations at \(-i(\rho-1/2)\), a phrase “compact support in a bounded strip,” and an initially divergent archimedean integral later replaced by a finite part. These formulas are not the recovered C15–C17 normalization, and no comparison was established.

[61_ATP_direct_obstruction.tex](/Users/raeez/chiral-bar-cobar-vol4/chapters/arithmetic/61_ATP_direct_obstruction.tex:46) defines the kernel with \(+\log\pi\), whereas C17’s completed factor yields \(-\log\pi\). A different decomposition could move a scalar term between contributions, so this discrepancy alone is not recorded as a proved false total formula. Next construction: fix one test function, transform convention, completed factor, and all polar/prime/gamma terms, then derive the equality. Confidence: high that correspondence is unresolved; no blanket refutation claimed.

**L06 — Live arithmetic action lacks the recovered evaluation data. HYPOTHESIS/TYPE GAP, severity 3.**  
[13_gaiotto_arithmetic_CS.tex](/Users/raeez/chiral-bar-cobar-vol4/chapters/arithmetic/13_gaiotto_arithmetic_CS.tex:81), lines 81–104, refers to an arbitrary number field and a compactified spectrum, writes an evaluated pairing with a fundamental class as an element of \(H^3\), and does not specify the evaluation map supplied in C30. Kim’s verified closed basic construction has the totally imaginary and coefficient hypotheses and values in \(\frac1m\mathbb Z/\mathbb Z\). The strongest recovered action is C30, with C31–C32 for boundary data. The broader live compactification/coefficient construction remains unresolved. Confidence: high on the missing interface, without claiming no such extension exists.

Live file hashes:

```text
13_gaiotto_arithmetic_CS.tex
7bd79f199a5edaf1397e4a00fc7d3d34455ea0aea372191653c7908bfee131f2
46_KMS_GNS_full_sector.tex
a704b37a946dca47ad1497085cd484bb20f34e171194078d1cc1ea74afef64f0
59_R_analytic_weil_gaussians_formal.tex
5120bfcfbc251446d363cdb7196b89b3cf024e814863bc32c92ffedc4956eb4b
61_ATP_direct_obstruction.tex
5c944bb8a00d0338cb2f5dca56a610cce5fbc98fb19c113f9cb10b2909d99c07
98_arithmetic_branch_residual_boundary.tex
d25f418a184fbc0fec6adc25f48dcd7053ca1a8f7ab134a20e3a48625011c28c
```

The residual-boundary chapter was read in full as the required arithmetic entry point. Its named global conclusions were not independently certified merely by following that routing instruction.

**Opening-context claims remain separately owned**

These were read as context, not accepted through their summaries:

| Context claim | Mathematical statement preserved | Residual and routing |
|---|---|---|
| Integral state lattice | Independent \(b_n\) in \(B(z)\), with logarithmic ghosts, support all integer-indexed fields and Hasse operations. | Read the all-field construction and base-change proof in Chapters 42–43; chapter starts belong to P011. |
| Integral flux classification | Framed momentum changes by integral two-forms alter \(H\) by \(dB\); Laurent de Rham torsion survives. | A classification proof on the precise torsion-free coefficient category is required; rational exactness does not decide integral equivalence. |
| Power covers | Level-changing \(\Phi_m\) acts on functions, \(B(z)\), and every momentum mode without dividing by \(m\). | Full mode identities and composition are not proved in P004’s spans. |
| Wild image and kernel | Wild-degree image is smaller than deck invariants; first Frobenius image is a regular commutant. | Exhaustion and nonreduced group-scheme invariants require the later cover calculations. |
| Modular singular center | Displayed \(p\)-power states exhaust the zero-flux singular center; higher Hasse translation remains. | Centrality alone is insufficient; exhaustion and operations remain later-chapter obligations. |
| Coordinate descent | Finite-jet integral coordinate action and Hasse overlap identities give a state sheaf/stratification. | Verify cocycles on every field and the coefficient-sensitive projective correction; Chapters 44–46 start in P012. |
| Torsion operation | \(3A=0\), \(15E=0\), \(TA=5E\), and \([Q_\lambda Q]=-A\lambda+TA\). | Exact orders and the nonzero three-primary operation require the later quotient computation. |
| Global-output Hochschild descent | \(C^*(A,A)\) is reconstructed from \(C^*(A_n,A)\), retaining global outputs and derived compatibility. | Chapter 36 starts at D6 byte `600415`, owned by P009. No full global-center acceptance follows from C38. |
| Rational torus and Rees claims in v5 | Closed-flux field construction, framed classification, flat Rees quantization, and cover laws. | These remain contextual statements requiring their own assigned chapter receipts and comparison maps. |
| Singular jet lattice comparison in v5 | Ordinary derivative and geometric arc lattices differ; the stated weight-eleven torsion is retained. | No decisive quotient calculation was read in P004; no arithmetic-reduction theorem is certified here. |

**F01 — Manuscript firewall. VERIFIED DEFECT, severity 3.**  
The recovered opening contains production history, archive availability, audit/certification language, and an “AI-assisted” attribution. The source interface at printed p. 75 also discusses the uploaded PDF and lossy extraction. These were confirmed visually in both editions. Such prose violates the supplied manuscript boundary. Preserve the mathematical hypotheses and open-problem statements; move production and review narration to coordination records. No manuscript edit was made.

**Complete unit-occurrence ledger**

Each row records the full unit identifier, both occurrences, and its distinct claim disposition. Unit hashes equal the identifiers and were verified individually. The two occurrences have identical mathematical text but are not independent corroboration.

| Unit SHA-256 | D6 sequence and bytes | D5 sequence and bytes | Disposition |
|---|---|---|---|
| `c2b062bb873b2890a07f9842b62433ec49490e7212ba13dfa2cbfd9b5db2cca1` | 83 `[198506,199354)` | 79 `[192803,193651)` | C01 survives |
| `8d8b0c95b97ce8dd6997f58d9c93a71ff5b6e4d61ffdb79a571b491212fa3a90` | 84 `[199354,200676)` | 80 `[193651,194973)` | C02; opening of C03 |
| `e5160367ec93147fabad2be96cb1bb45cc180c16e0732ff17e7b2874e00caab8` | 85 `[200676,202340)` | 81 `[194973,196637)` | C03 survives; trace-class continuation excluded |
| `c6c47818186789272cfd5ea70a6f4fc9b829cd42e64957c88e475c544571223f` | 86 `[202340,204365)` | 82 `[196637,198662)` | C04; hypotheses of C05 |
| `8790e9b4bfea3f7472e374f3edc56114a12b3b1bd24c250eb66db4dc58c994ea` | 87 `[204365,204925)` | 83 `[198662,199222)` | C05 operator/product statement |
| `142183845f58e51dd4c184ef93a17dfd6800cd9ce47b9ab9b0ccfe5a7b515179` | 88 `[204925,206791)` | 84 `[199222,201088)` | C05 proof and C06 obstruction |
| `e707314d9e4a27441f93e5e3c1ee0e227479e0a9da31999acb242ed1c367aced` | 89 `[206791,209105)` | 85 `[201088,203402)` | C07 imported theorem verified; C08 setup |
| `58472f4afc8ffb04811d8832f5eb57ec7d0a7c4d862c7fe79f36fc6aba620b6b` | 90 `[209105,209976)` | 86 `[203402,204273)` | C08 moments and uniqueness survive |
| `b4a75d35a4fa7f9bec4e2f81eddd794c520a5a40e3d61c9c5ed2e751a5092178` | 91 `[209976,210833)` | 87 `[204273,205130)` | C08 existence; C09 inductive-limit setup |
| `62b532db8358f418f6a2d5192a05e13d7e47a9d0e46857abdc46bd775b97e2ad` | 92 `[210833,211460)` | 88 `[205130,205757)` | C09 threshold statement |
| `64b1fff3a56d546d2dfdcc9ce692270a35a1269f09a64ad7024df46220fea04d` | 93 `[211460,217421)` | 89 `[205757,211718)` | C09 survives; C10 defect; C11–C14 qualified as above |
| `da51466ef9dda9acea2860734626a45e62b04342e2e73c9d9f9f8cfb4c7b34a6` | 94 `[217421,218949)` | 90 `[211718,213246)` | C14 positivity boundary; C15 definition |
| `7cde1848f4953254c3af63e2a611cb4d877047e6ffdfed94ef9dec9b6d68c9d1` | 95 `[218949,221064)` | 91 `[213246,215361)` | C15 survives; C16 hypotheses |
| `e562c4237d3771a088c5eea535ea5bac0aa7bf78bfa29acb4de6190402f37d98` | 96 `[221064,225087)` | 92 `[215361,219384)` | C16 estimates; C17 statement; named source gate remains |
| `f51fee3d244e71d5b93cfed71c90b04473305472645ae3a7f400bf8f668f1b09` | 97 `[225087,230338)` | 93 `[219384,224635)` | C17 contour proof; C18 interpolation setup |
| `c6f434ce68cb6334c8c3a404945d2c0c2baff62bc0df3eb50dc6187168930987` | 98 `[230338,232708)` | 94 `[224635,227005)` | C18 detection proof and criterion survive |
| `d3a36d95c766e181874fe4ddcf2cf8b080b192595068d842ca567094e96731c7` | 99 `[232708,234238)` | 95 `[227005,228535)` | C18 criterion scope; C19 kernel sign |
| `0942b0aac2b60a43a7c68a778a79681dde5a88b72e12185d5de04e082cd2f603` | 100 `[234238,235480)` | 96 `[228535,229777)` | C19 negative gamma example survives |
| `ce0aa62776be999df88c487839ae1be2d4ecfbdee3ac27af3c11fc5c7a79f15c` | 101 `[235480,239404)` | 97 `[229777,233701)` | C19 gap obstruction; C20; F01; C21 setup |
| `8f144f28520627bcef7a2e1422b0efd9afaf50d48e78a4f40ec60cb9d050b57b` | 102 `[239404,239990)` | 98 `[233701,234287)` | C21 orbit inversion survives |
| `b27de930a58d5c00a1ce07ef87f07c26a62e63cd8d6b9008232be72753f931ac` | 103 `[239990,243304)` | 99 `[234287,237601)` | C21 formal product; C22 divisor model |
| `d43494eb0479e8c506283642da37858ba7c40ca22a6665807129a3c9a867ccae` | 104 `[243304,245778)` | 100 `[237601,240075)` | C23 carrier gap; C24 determinant identity |
| `126470262c49d6b10de7b907f7396d182558ba751017b330947392d6e6d497f0` | 105 `[245778,247851)` | 101 `[240075,242148)` | C24 information loss/supertrace; C25 finite example |
| `23b16dc35b8007c2f32cb17c62ac693959993266fbbe55ca8d619d10991ad3f8` | 106 `[247851,250950)` | 102 `[242148,245247)` | C25 finite verification; C26 obstruction; C27 scope |
| `c1a29aec5fb824583928a0ee0c88c1d3d37ef46a62203bd71469197136faacb1` | 107 `[250950,254396)` | 103 `[245247,248693)` | C27 comparison residual; C28 coherence |
| `310b5465ee3b537a6516c3cf895d49f1f2f8816a2063671b60d9789524646cea` | 108 `[254396,256143)` | 104 `[248693,250440)` | C29 coefficient obstruction; C30 hypotheses |
| `9f92cce1934dfed2e1929a7167fd81a30c9ae6b3500fd02f8577b58ac7b144c8` | 109 `[256143,257683)` | 105 `[250440,251980)` | C30 action/invariance; C31 definition |
| `b4c5edf5a4801885551bbf62617be642cedaf198bad847926e5df398deff5570` | 110 `[257683,261248)` | 106 `[251980,255545)` | C31–C32 torsors; C33 finite sum |
| `382cc6e6cdb84c3f181d256462d2766f1001ada1aaec43867f38e4bdd9a162a5` | 111 `[261248,262856)` | 107 `[255545,257153)` | C33 finiteness/nonzero denominator; C34 typed observable |
| `9ebe37af97b28971d8755f657827243833d47dfcce16c270d4665a21ede6c028` | 112 `[262856,263803)` | 108 `[257153,258100)` | C34 averaging and first-trace obstructions |
| `1ef2087399a4912ecbd1108529627bf274257219310ed27c1a0dca5c2ec89105` | 113 `[263803,265667)` | 109 `[258100,259964)` | C35 limit residual; C36 center distinction |
| `e41f4af39d85cf4be641bf710081027aa3c70451530ea2e6d904f3bb90300b2e` | 114 `[265667,268580)` | 110 `[259964,262877)` | C36 definitions; C37 differential, completed with adjacent context |

**Boundary dependencies and remaining verification**

- Incoming owner P003: D6 boundary `198506`, D5 boundary `192803`. The additional gamma normalization was read directly; no acceptance of P003’s other claims is implied.
- Outgoing owner P005: D6 boundary `268580`, D5 boundary `262877`. Required adjacent context completed the diagonal-resolution and cup-model arguments, but supplies no separate ownership credit.
- Chapter 3 context lies within P002’s spine. Its complete definitions, contraction, and comparison were independently read for C37–C38.
- Later global descent and integral fields remain with P009, P011, P012, and the lead’s remaining routing. Their preface summaries are not substitutes for proofs.
- Exact comparison with the cited older *Surviving Theory* propositions was not completed. Those critique-reference assertions remain provenance leads, not verified edition correspondences.
- Primary-source verification remains incomplete for the exact Jensen/Hadamard and original Weil citations. No unavailable check is marked passed.
- Requested runtime model and effort remain unverified; no mathematical certification should silently convert the requested controls into observed controls.

The finite checks used Node `v25.2.1`; PDF inspection used Poppler `26.02.0`. Exact arithmetic gave \(32\) points over \(\mathbb F_{25}\), the six stated projective-line orbit counts, and no carry-identity failures in the specified finite range. No numerical approximation was used to certify the general arguments.

The next live repair should begin with L01’s inconsistent state, then rederive the GNS carrier and modular signs before transferring any pairing or positivity claim.
