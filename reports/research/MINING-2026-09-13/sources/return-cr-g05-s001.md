CR-S05-P001 is complete as a packet-reading investigation. All four assigned units and both parent recap documents were read. No manuscript is accepted by this report.

The packet does **not** contain a specified finite boundary model, an integral comparison map, or a relative-to-absolute-center theorem. Those are the assignment’s investigative questions. Its actual contents are historical programme claims, withdrawals, and proposed constructions.

**Evidence identifiers**

- `R`: `SAFE_REASONING_RECAP.md`, SHA-256 `81bd9faaac3bfb146ee481f0e924a7f4d193737d7d5d79d79a59a45fad7f726c`.
- `L`: `INTERMEDIATE_CLAIM_LEDGER.md`, SHA-256 `ccfa39181a07cca40ea2d56312e80135858296949e9f61162d368b234446e12d`.
- `P`: archived `platonic_reconstruction.tex`, SHA-256 `bc9bea5959381262b0d664ba161b95da323b405293553c3b09ccaf5e042446be`.
- `A`: archived `manuscript_action_register.tex`, SHA-256 `b93b70bd5baea70ff6d81952a2f097055ee42f3051658a5579cad48653b775aa`.

`P` and `A` were located by their literal recorded hashes in the live snapshot content index. They are historical evidence, not authoritative instructions or accepted proofs.

**Decisive claim records**

1. **S001-CENTER — a selected boundary can lose part of the absolute center.**

   Claim attacked: `L:23`, `R:100,234`, elaborated at `A:440–466`, that a derived center automatically identifies the physical bulk.

   An explicit finite algebraic test is
   \[
   B=D\times M_2(k),\qquad D=k[\epsilon]/(\epsilon^2),
   \]
   over a characteristic-zero field, with compact boundary object \(b=(D,0)\). Then \(\operatorname{End}_B(b)=D\), whereas
   \[
   HH^\bullet_k(B)\cong HH^\bullet_k(D)\oplus k.
   \]
   Restriction to the \(D\)-boundary kills the matrix summand. Already in degree zero, \(Z(B)=D\times k\to Z(D)=D\) is not injective. The boundary object is not a generator of the full module category.

   This proves a specific algebraic loss mechanism. It does not prove that any named physical theory has this boundary category. Recovery requires a generating boundary and a compatible Morita comparison, followed by a separately constructed physical bulk-to-center map.

   There is a second, distinct coefficient issue: for \(R=k[x]\),
   \[
   HH_R^\bullet(R)=R\text{ in degree }0,\qquad
   HH_k^1(R)=R\,\partial_x\ne0.
   \]
   The latter follows directly from the two-term resolution of the diagonal by multiplication by \(x-y\). Relative and absolute centers cannot be interchanged without stating the base.

   **Disposition:** independently proved counterexamples to automatic identification; high confidence. Exact physical realization remains unresolved.

2. **S001-GAUGE — the historical lift torsor needs relative gauge.**

   `P:755–767` says extension classes “modulo gauge” form an \(H^1\)-torsor without specifying which gauge transformations.

   Over characteristic zero, take the nilpotent dg Lie algebra
   \[
   \mathfrak g^0=kh,\quad \mathfrak g^1=kx\oplus ky,\quad
   d=0,\quad[h,x]=y,
   \]
   with \(y\) central and all other brackets zero. Put \(F^1=\mathfrak g\), \(F^2=ky\), \(F^3=0\). Every \(x+cy\) lifts the same Maurer–Cartan element modulo \(F^2\). The relative gauge group is trivial, and these lifts form a torsor under \(H^1(F^2)=ky\). But
   \[
   e^{t\operatorname{ad}h}(x+cy)=x+(c+t)y,
   \]
   so quotienting by the full gauge group gives one orbit, not an \(H^1\)-torsor.

   The live paper expressly repairs this distinction: [paper.tex:154](/Users/raeez/mixed-ht-total-obstruction/paper.tex:154) states the torsor only after quotienting by transformations reducing to the identity on the base; lines 200–205 explain the remaining base-stabilizer action.

   **Disposition:** historical ambiguity with a proved counterexample to the unrestricted reading; high confidence. It is not a defect of that current relative statement.

3. **S001-TOTAL — projected obstruction vanishing is insufficient.**

   Claim attacked: `L:28`, `R:170,237,269`.

   In the cohomologically graded dg Lie algebra
   \[
   \mathfrak g^1=kx,\quad\mathfrak g^2=kz,\quad
   d=0,\quad[x,x]=2z,\quad z\text{ central},
   \]
   with \(F^2=kz,F^3=0\), the curvature of \(x\) is \(z\ne0\), although its projection to \(\mathfrak g/F^2\) vanishes. Repeating that projection in multiple rows supplies no additional detection.

   The recoverable construction is the one-stage central-extension theorem: curvature defines a class in \(H^2(F^r/F^{r+1})\); its vanishing permits a correction in degree one. A compatible infinite family gives an actual Maurer–Cartan element only under the required completeness and separation conditions. The elementary proof checks the curvature in every quotient and then uses degree-two separation.

   Current exact counterparts are [paper.tex:60](/Users/raeez/mixed-ht-total-obstruction/paper.tex:60), its one-stage theorem, and [paper.tex:754](/Users/raeez/mixed-ht-total-obstruction/paper.tex:754). The live mixed-HT introduction, [main.tex:290](/Users/raeez/mixed-holomorphic-topological-strings/main.tex:290), calls the global map a **criterion** and lists required primitives.

   **Disposition:** the general inference is disproved; the current criterion does not make that inference. A constructed native total carrier and its actual global solution remain separate obligations.

4. **S001-FINITE — finite algebra and trace survive; unrestricted closed-surface interpretation does not follow.**

   An actual live finite model occurs at [part3_examples.tex:257](/Users/raeez/chiral-bar-cobar/reconstruction/core/part3_examples.tex:257):
   \[
   B_n=k[\epsilon]/(\epsilon^2)\times M_n(k),\qquad
   \varepsilon_B(a+b\epsilon,M)=a,\qquad
   \tau_B(a+b\epsilon,M)=b+\operatorname{Tr}M.
   \]
   The trace pairing is perfect. The augmentation is multiplicative. The augmentation module sees the dual-number factor, giving one-dimensional \(\operatorname{Tor}_r^{B_n}(k,k)\) in every nonnegative degree. The algebra is finite-dimensional, but its bar is not bounded in bar length.

   Direct dual-basis contraction gives
   \[
   e_B=(2\epsilon,nI_n),\quad
   \tau_B(e_B)=2+n^2,\quad
   \tau_B(e_B^g)=n^{g+1}\quad(g\ge2).
   \]
   These are valid algebraic calculations.

   The promotion at [part4_physics.tex:314](/Users/raeez/chiral-bar-cobar/reconstruction/core/part4_physics.tex:314) calls these quantities closed-surface genus amplitudes. The earlier ribbon theorem specifies a **positive-boundary** graph action. That does not itself supply operations for surfaces with no boundary. Moreover, noncommutative open state algebra, Hochschild closed states, and a commutative closed TFT algebra are different carriers. For \(n=2\), \(\tau_B(e_B)=6\), while \(\dim HH_0(B)=\dim Z(B)=3\). This comparison is a diagnostic of carrier change, not by itself a universal formula for the TCFT torus.

   Costello’s Theorem A constructs a homotopy-universal open–closed extension and identifies its closed-state homology with Hochschild homology; it does not license replacing the closed sector by the original noncommutative algebra. [Costello, Theorem A, physical page 8](https://arxiv.org/pdf/math/0412149).

   **Disposition:** finite augmentation, bar, and trace computations verified. Closed-surface promotion has an unresolved domain/operation gap, severity 2 if used to support all-genus physical amplitudes. Next check: specify the permitted surface category, closed state complex, and cap/handle operations.

5. **S001-CYCLIC-INTEGRAL — finite truncation and rational comparison need separate compatibility proofs.**

   There is no such comparison map in the assigned packet. The following deciding examples establish the necessary obligations:

   - On \(A_N=k[x]/(x^{N+1})\), the Frobenius functional \(\tau_N(x^i)=\delta_{iN}\) is nondegenerate. But the quotient \(A_{N+1}\to A_N\) does not preserve these traces: evaluate \(x^N\). Thus individually perfect finite models need not form a compatible cyclic inverse system.
   - The complex \(\mathbb Z\xrightarrow{p}\mathbb Z\), in degrees \(0,1\), has \(H^1=\mathbb Z/p\), which disappears over \(\mathbb Q\). Rational equivalence does not establish an integral equivalence.
   - Averaging invariant primitives requires division by two. For \(d:\mathbb Z^2\to\mathbb Z\), \(d(a,b)=a+b\), with involution exchanging coordinates, \(1\) has a primitive but no invariant integral primitive. `P:784–799` works over \(\mathbb C\); its averaging argument cannot be imported unchanged over \(\mathbb Z\).
   - Completion and localization do not generally commute:
     \[
     \widehat{k[t]}_{(t)}[t^{-1}]=k((t)),\qquad
     \widehat{k[t,t^{-1}]}_{(t)}=0.
     \]
   - The rank-one sewing model in the live source assumes \(\lambda\in k^\times\); its inverse pairing is \(\lambda^{-1}\). It does not extend to \(\lambda=0\) by substitution.

   **Disposition:** independently proved finite counterexamples; high confidence. They refute unconditional transfers, not every possible integral or completed construction. The strongest recovery is a compatible system retaining multiplication, all higher operations, traces, base-ring data, and continuous comparison maps.

6. **S001-LATTICE — the integral level-six calculation survives at its stated carrier.**

   `R:178–186` and `P:923–1021` give \(\Lambda=\mathbb Z^4\), \(\delta=(-2,-1,3,0)\), \(\psi=e_4^*\), and
   \[
   \Xi=
   \begin{pmatrix}
   0&3&1&0\\-3&0&-2&0\\-1&2&0&-2\\0&0&2&0
   \end{pmatrix}.
   \]
   Independent integer arithmetic gave
   \[
   \delta^{T}\Xi=(0,0,0,-6),\qquad
   \text{determinantal divisors }(1,1,6,36),
   \]
   hence Smith invariants \((1,1,6,6)\). Therefore
   \[
   \iota_\delta\xi=-6\psi,\quad
   \ker\psi=\delta^{\perp_\xi},\quad
   \operatorname{coker}\xi^\flat\cong(\mathbb Z/6)^2.
   \]
   Since \(\delta\) is primitive, \(\ker\psi/\mathbb Z\delta\) has basis \([e_1],[e_3]\), whose pairing is \(1\).

   On \(\mathbb C^6\), \(X|r\rangle=|r+1\rangle\) and \(Z|r\rangle=\zeta_6^r|r\rangle\) satisfy \(ZX=\zeta_6XZ\). Distinct \(Z\)-eigenlines and transitive \(X\)-action prove irreducibility. This supplies a finite Heisenberg representation; it supplies no vertex operators, conformal vector, anomaly cancellation, or QFT state-space comparison.

   **Disposition:** exact lattice and representation calculations verified; high confidence within this algebraic scope.

7. **S001-TRANS — preserve the affine determinant, specify the transgression carrier.**

   `R:190–196`, `P:1027–1121` define
   \[
   G=\langle c,x_0,x_1\mid c\text{ central},\
   x_0x_1=1,\ x_0^r=c^m,\ x_1^s=c^n\rangle .
   \]
   Eliminating \(x_1\) gives the abelian relation matrix
   \[
   \begin{pmatrix}r&-m\\s&n\end{pmatrix},\qquad D=rn+sm.
   \]
   For \(D\ne0\), its invariant factors are \(d_1=\gcd(r,s,m,n)\) and \(|D|/d_1\). For \(D=0\), the rank-one case retains a free \(\mathbb Z\)-summand. The test \((r,s,m,n)=(3,4,1,-1)\) gives \(D=1\).

   The general “integral affine transgression” passage needs more than this presentation: specify the orbifold or coarse-base Leray carrier, local-system lattices, integral image of the fiber character, orientation, and global Euler/clutching normalization. A singular Seifert quotient cannot silently be treated as an ordinary circle bundle over its coarse base.

   **Disposition:** Smith arithmetic proved. The asserted general geometric transgression is conditional on missing carrier and normalization data. The explicitly sourced Engel \((3,4)\) calculation is a distinct instance, not proof of every \((r,s)\) realization.

**Every historical ledger row**

The following records preserve the original question and historical dismissal. “Unverified” means the supplied source does not provide enough information for a theorem-level verdict about its named manuscript.

| ID / source | Claim, critique, recoverable construction, and next obligation |
|---|---|
| H01 — `L:7`, `R:45` | **Twist obstruction from the canonical bundle.** The alleged revision by a companion manuscript is not accompanied by its exact theorem or square-root construction. Even a line \(K^{1/2}\) does not specify the self-dual quantum field. Recoverable: twisting data. Next: the companion’s actual line bundle, supersymmetry/twisting map, and global field complex. **Unverified; high confidence in the missing-source diagnosis.** |
| H02 — `L:8`, `R:45`, `A:T.1` | **Fully engineered abelian six-dimensional \((2,0)\) theory.** The intended spacetime is the proposed complex six-sphere with singular torus fibration. The packet gives no BV/BRST fields and ghost degrees, action, flux lattice, quadratic refinement, gauge fixing, propagator, anomaly trivialization, or nonperturbative sectors. Recoverable: a proposed protected twist. Next: differential cocycles and a relative self-dual theory with gluing. **Unsupported existence assertion; no physical no-go proved.** |
| H03 — `L:9`, `R:46`, `A:T.2` | **Proper pushforward produces the desired VOA.** The proposed map is the torus fibration to \(\mathbb P^1\). A factorization pushforward is a sensible first construction, but the source contains no specified observable algebra or proof of holomorphic translation structure, vacuum, grading finiteness, singular behavior, or completion. Next: construct those data on the smooth locus and at all singular fibers. **The automatic implication is unsupported.** |
| H04 — `L:10`, `R:47,49`, `A:T.3` | **Affine shifts give complete orbifold defects.** Orders \(3,4\) and affine torsion shifts describe geometric actions. No twisted state spaces, cocycles, group-cohomological anomaly, sewing, or modular covariance are supplied. Narain momentum/winding completion is a proposed remedy, without its lattice, metric, or comparison. **Keep geometric quotient data; full defect theory unresolved.** |
| H05 — `L:11`, `R:50,57` | **Rank-four local system is a positive Seiberg–Witten system.** The historical critique concerns positivity of the polarization, not merely rank. The primary paper states an indefinite Hodge form in Remark 8.4. A rank-two Maxwell subsystem is a proposal; no special-Kähler data, Seiberg–Witten differential, spacetime, Maxwell action, coupling, surface-defect boundary conditions, or observable comparison is constructed here. **Naive positive interpretation fails for that supplied form; replacement unresolved.** |
| H06 — `L:12`, `R:71`, `A:T.4` | **\(S^6\to S^3\) is a generator.** A quotient map does not calculate its homotopy class. Recoverable: the quotient question. Next: a smooth representative, regular-value framed fiber, and an actual unstable homotopy calculation; stable invariants alone need a proved detecting comparison. **Unverified generator claim.** |
| H07 — `L:13`, `R:68`, `A:T.5` | **The \(u\)-parameter canonically splits cusp monodromy.** Naming a second parameter produces no commuting nilpotent residue. Next: a two-parameter semistable family, logarithmic connection, residues, and limiting Hodge data. **Unresolved, not disproved by the recap.** |
| H08 — `L:14`, `R:69`, `A:T.6,T.8` | **Divisor classes equal knot-linking/Atiyah charges.** No map between Picard/cohomological data and the chosen link complement is stated. Recoverable: a comparison problem. Next: construct the quotient skeleton, cycles, orientations, and invariant comparison. The further phrase “complex topology” provides no construction. **Unverified.** |
| H09 — `L:15`, `R:70,106`, `A:T.7` | **Cusp realizes \(E_6/W_3(3,7)\).** The shared integers do not define the singularity category, defect algebra, VOA, or physical theory. Next: a vanishing-cycle/matrix-factorization construction and a functor preserving monodromy, fusion, grading, and characters. **Unsupported identification; no general impossibility proved.** |
| H10 — `L:16`, `R:90` | **Functional equation/Koszul duality implies RH.** The elementary symmetric polynomial \(f(s)=(s-\tfrac14)(s-\tfrac34)\) satisfies \(f(1-s)=f(s)\) with off-line zeros. Thus symmetry alone cannot force critical-line support. This does not attack RH with all zeta-specific hypotheses. Recoverable: independent positive adjoint structure plus a determinant-divisor theorem. **Automatic symmetry implication disproved.** |
| H11 — `L:17`, `R:91` | **Li coefficients are Virasoro norms.** Neither an independently positive representation nor the exact Gram comparison is supplied. Naming a form a norm assumes its positivity. Next: construct representation, adjoint, common domain, state, and normalization before proving the identity. **Circular route identified; specific manuscript equality unverified.** |
| H12 — `L:18`, `R:92–94,130`, `P:615–693` | **Prime-gas/Bost–Connes Hamiltonian is Hilbert–Pólya.** On \(\ell^2(\mathbb N)\), \(H e_n=(\log n)e_n\), with maximal square-summability domain, has heat trace \(\sum n^{-s}\) for \(\Re s>1\). That calculation establishes its logarithmic energy spectrum, not a zero-spectrum realization. Placing zeros on a diagonal and asking for a positive self-adjoint centered operator restates critical-line support. **Recover the Euler trace and conditional Deninger theorem; independent zero operator unresolved.** |
| H13 — `L:19`, `R:95,138` | **Two oscillators produce a \(GL_2\) Whittaker model.** The recoverable character calculation is \(\sum h_mz^m=((1-\alpha z)(1-\beta z))^{-1}\), with \(h_m=(\alpha+\beta)h_{m-1}-\alpha\beta h_{m-2}\). It constructs symmetric-power characters. A \(GL_2(\mathbb Q_p)\)-action and a nondegenerate Whittaker functional are additional data. **Character calculation valid; representation identification unsupported.** |
| H14 — `L:20`, `R:96` | **Arbitrary local angles globalize.** The source gives no global representation, central character, ramification conditions, or globalization theorem. Recoverable: calculations conditional on a genuine global automorphic representation. **Unverified general claim; no exact proposed globalization theorem supplied to refute.** |
| H15 — `L:21`, `R:97–98,142` | **Ordinary BD geometry on \(\operatorname{Ran}(\operatorname{Spec}\mathbb Z)\).** The ordinary smooth-curve \(D\)-module formalism and CRT data are different inputs. Recoverable: coprime residue factorization. A further typing defect appears at `P:115–120`: a tensor product defined only for coprime integers is not an ordinary everywhere-defined monoidal product. Use a partial/disjoint-support structure or a specified enlargement. **Typing objection verified; alternative arithmetic geometry remains open.** |
| H16 — `L:22`, `R:99,166` | **Complex locality gives positivity.** The complex \(*\)-algebra \(\mathbb C^2\) admits both the positive normalized functional \((a+b)/2\) and the normalized nonpositive functional \(2a-b\). The algebra alone chooses neither. `P:700–720` correctly transfers positivity through a state-preserving \(*\)-isomorphism on \(H^0\). **Automatic implication disproved; physical reflection/state comparison unresolved.** |
| H17 — `L:23` | **Derived center equals physical bulk.** See S001-CENTER. The physical arrow requires a specified theory, boundary coupling, central action, and proof of equivalence; algebraic universality does not construct gauge fixing, quantum states, or anomaly cancellation. |
| H18 — `L:24`, `R:101`, `A:V2.12–V2.15` | **Virasoro boundary algebra is complete three-dimensional gravity.** The actual physical target is an AdS\(_3\)-type gravity interpretation. The source supplies no metric/Chern–Simons path integral, real form, contour, modular pairing, saddle sum, or nonperturbative sectors. Its surviving object is boundary symmetry or a protected sector after a supplied realization. No exact Brown–Henneaux or Maloney–Witten theorem locator is supplied here. **Equality unsupported; no gravity impossibility proved.** |
| H19 — `L:25`, `R:102`, `A:V3.1–V3.8` | **Abstract CY category canonically gives the intended spacetime theory.** A categorical trace does not specify the intended sheaf of fields, action, opens, boundary conditions, or propagator on \(X\). The objection concerns that physical/geometric realization, not the possibility of some constant factorization construction. Recoverable: an equipped geometric CY/BV datum and actual pushforward. **General physical implication unsupported.** |
| H20 — `L:26`, `R:103–104,174` | **Denominator or partition function determines an algebra/QFT.** The abelian Lie algebra on graded basis \(x,y,z\) of degrees \(1,1,2\), and the algebra with \([x,y]=z\), have identical graded dimensions and different derived algebras. Likewise \(0\) and a nonzero \(2\times2\) nilpotent Jordan block have determinant \(s^2\). Recoverable: a constructed graded surjection plus finite-dimensional equality in each degree, followed by compatible completion. **Scalar recovery disproved.** |
| H21 — `L:27`, `R:105,162` | **RH and prime gaps are one spectral problem.** The historical formulations have different quantifiers: universal positivity of a Weil form versus existence of a vector with sufficiently large positive correlation quotient. That separates the stated criteria; it does not prove no future coupling can exist. Next: an explicit coupling preserving both arithmetic statements and analytic thresholds. **Blanket impossibility would overstate the evidence.** |
| H22 — `L:28` | **Ten obstruction rows construct the global theory.** See S001-TOTAL. In physics this also requires actual renormalized QME data, counterterms, scale compatibility, descent, and an anomaly primitive. A formal dg Lie algebra alone supplies no all-loop or nonperturbative existence theorem. |
| H23 — `L:29`, `R:186` | **Level-six data automatically give VOA/QFT.** See S001-LATTICE. Finite Heisenberg quantization survives. Metaplectic transport, geometric state spaces, vertex operations, stress tensor, anomaly, and sewing are residual constructions. |

**Additional claims in the recap**

- **R:28–37, geometric assertions.** The current Engel PDF supplies exact locators: the surface equation and height computation in §2, Lemma 2.1 and Corollary 2.2; contraction and quotient in Propositions 2.4–2.6; torsion conditions in Corollary 3.9; invariant covector in Lemma 3.10; fundamental group in Proposition 6.1; integral differentials in Lemma 7.6 and homology in Theorem 7.7. The contraction requires sufficiently small nonzero \(u\), not merely a section with a simple zero. Torsion shifts must satisfy the primitive conditions. The unit condition concerns the constructed \(Y\) with those hypotheses. These are source correspondences, not a fresh verification of the whole geometric proof. [Engel, §§2–7](https://philip-engel.github.io/S6.pdf).
- **R:34, cusp directions.** The relevant integral condition is rank-two primitive monodromy image together with \(N_\infty^2=0\). It does not establish an external two-parameter family. The excerpted matrix calculation requires the full marking/degeneration comparison for geometric certification.
- **R:51–52, additional physical proposals.** Chiral de Rham and holomorphic BF are separate proposed constructions. The recap gives no chiral-de-Rham theorem locator and no BF action. I did not reinterpret either as an already quantized \((2,0)\) theory.
- **R:114–126, spectral replacements.** `P:617–639` gives the diagonal tautology with its maximal operator domain. `P:669–691` gives a valid conditional sufficiency argument from a closed densely defined \(\Theta\), equality of adjoint domains, \(\Theta^*=I-\Theta\), and a determinant with the exact zero divisor. It constructs none of those arithmetic inputs.
- **R:134, Weil/GNS.** `P:526–599` assumes an admissible unital test algebra or unitization and an appropriately extended Weil functional. Its algebraic radical quotient is meaningful under those assumptions. Positivity on a nonunital test algebra does not automatically provide the claimed positive unitization and cyclic vector. The exact test space, functional, extension, and primary Weil locator remain unverified here.
- **R:142–158, arithmetic constructions.** CRT factorization, singular-series convergence, finite incidence Gram forms, and the continuum Maynard operator are context owned by `coverage-0363`. Their proofs were not independently certified in this assignment. In particular, a finite Rayleigh calculation does not establish the required asymptotic distribution transfer.
- **R:166–170, dagger and obstruction replacements.** The \(H^0\) state-preserving transfer is directly justified by preservation of \(\omega(a^*a)\); it does not transfer a complete physical theory. The obstruction construction retains the relative-gauge and completion qualifications recorded above.
- **R:198–227, artifact history.** The two recorded TeX hashes match actual snapshot contents. Their line counts are 1,327 and 1,207. I did not verify the claimed historical builds, ZIP tests, or README checksum, and executed no archived command.
- **R:233–239, named-volume actions.** These are proposed decompositions, not theorem statements: Volume I bar–cobar/comparison; Volume II center/existence/recognition/topologization; Volume III native/specialized/Hall/double; Volume IV arithmetic separation; mixed-HT total obstruction; Igusa classical versus compact realization; \(S^6\) geometric versus protected-theory comparison. No action is evidence that its corresponding manuscript was repaired.
- **R:256–271, “surviving architecture.”** The displayed local-to-global sequence is a proposed research architecture. It provides neither a global construction nor a unit, norm, positivity, QME, or recognition theorem. Each of its stated hard problems remains separately scoped.

**Exact live correspondence and physical limits**

The inspected repository heads were unchanged and had no tracked working-tree changes at the beginning and end of inspection:

| Repository | Observed HEAD | Relevant source relationship |
|---|---|---|
| `chiral-bar-cobar` | `cb6e88263f4bb75ef5c1d9db911f61ca5d3d4d9c` | Active integrated source includes both the short Volume-I chapter and `reconstruction/core/*`. The boundary-center qualification appears in `part2_duality.tex:307–322`; the finite trace model appears in `part3_examples.tex:257–296`; its sewing use appears in `part4_physics.tex:180–386`. |
| `calabi-yau-quantum-groups` | `aaf325a7b7c4d9a8da252ce1a8db5448e5300aa9` | The integrated CY chapter separates categorical outputs, an independently specified local BV theory, boundary observables, and actual-map pushforward. The older `chapters/theory/cy_to_chiral.tex:370–610` retains substantially stronger stage-one and specialization assertions. These are different source surfaces and cannot receive one shared verdict. |
| `mixed-holomorphic-topological-strings` | `fbe902d8dd1b7428db392028f7899c1f5d8ab2e1` | `main.tex:260–430` distinguishes the stable trace theorem from the global criterion and preserves separate \(\hbar_{\mathrm{QME}},\hbar_{\mathrm W},\hbar_\omega,\hbar_{\mathrm{Rees}}\). |
| `mixed-ht-total-obstruction` | `9e55b0a3c09e78ceaf6f2480b9a22e3997a88de4` | `paper.tex:60–205,754–790` supplies the explicit projected-curvature example, relative lift theorem, and representative-limit theorem. No physical mixed-HT realization follows solely from them. |

The live free BF example states spacetime \(X^{an}\times\mathbb R\), with \(X\) a complex curve,
\[
A\in\Omega^{0,*}(X)\widehat\otimes\Omega^*(\mathbb R)\otimes V[1],\quad
B\in\Omega^{1,*}(X)\widehat\otimes\Omega^*(\mathbb R)\otimes V^*[-1],
\]
and \(S=\int\langle B,(\bar\partial+d_t)A\rangle\). The preceding realization theorem explicitly assumes renormalized graph weights, face compatibility, QME, algebraization, and local constancy. I read this as a different local field model, not a constructed comparison to the six-dimensional theory.

The integrated CY source states holomorphic Chern–Simons fields \(\Omega^{0,*}(X,\mathfrak a)[1]\) on a complex threefold with volume form, and the quadratic-plus-cubic action with coefficients \(1/2,1/6\). Its classical Maurer–Cartan identity does not supply gauge fixing, propagators, a renormalized quantum action, or an anomaly trivialization. Its one-loop anomaly assertion was not independently verified against the cited primary source in this assignment.

The archived bibliographies name only “work in progress, 2026” editions. Their Volume-II and Volume-III title forms even differ between `P` and `A`. They provide no source commit or PDF hash for those citations. Consequently, exact correspondence to each originally named edition remains unresolved. No separate “Core” repository is asserted.

**Complete read ledger**

Common fields:

```text
assignment_id: CR-S05-P001
frozen_supplemental_manifest_sha256:
  01dcdb8978f13296ccc4dece9fde1ba5205a1b7d70c3230d54a3fd2e5870691f
supplemental_allocation_sha256:
  f0ed7cc7d526e4e521961456d6f151c027c4d1b059bb998314affb4d0d824b80
supplemental_inventory_sha256:
  6ebcfcbbc217ec96a0a0c846ae85a567abe3f8736c45057caf1491be4be8f8f2
reader_contract_sha256:
  4c9cd2fcda6930663e88433a090cc3199cb8a8b406ce246dc83851ece0d0b927
packet_id: 100--programme--transcript--76605ec48fddadfa
packet_sha256:
  a0d58335f995052fb07b871093e2e5b6bb244607876bf4e6e4973034d66f56f1
packet_bytes_actually_read: [0,10697)
requested_model: gpt-6-astra
requested_reasoning_effort: ultra
observed_model_and_effort: unavailable; unverified
changed_paths: []
```

All hashes above matched. The assignment was selected uniquely by its literal `assignment_id`; all fields were exposed and read.

| Every assigned occurrence | Actual source reading | Claims/disposition | Missing context / next check |
|---|---|---|---|
| Unit `a7776d05afbe84fa1906b10aae499549548e3c46f186e8543cc158b0a54ed97d`; `R`, sequence 0 | `[0,2690)`, lines 1–50; hash matched | Geometric claims and H01–H05. Complete reading; conditional/source-limited dispositions above. | Original cited editions; full physical model; remaining geometric proof dependencies. |
| Unit `48ddf3cdccb889a0e2074079ab0773d5abad32a2352af6006b7e1e1183c32fc7`; `R`, sequence 4 | `[10805,13530)`, lines 216–271; hash matched | Artifact history, seven named-volume actions, common architecture. Complete reading; no acceptance inference. | Historical build evidence; exact edition comparison; each missing construction. |
| Unit `0f88c36286fe8953430423b2f972aecf61b511c4e3d05c3622a5de50fc57f6d5`; `L`, sequence 0 | `[0,3173)`, lines 1–22; hash matched | H01–H16. Complete reading. | Per-row residuals above. |
| Unit `6936e2ac743c9aaa7753c03e17c6f0cbd20b81389fee1c924a3785aad40c9f88`; `L`, sequence 1 | `[3173,4388)`, lines 23–29; hash matched | H17–H23. Complete reading. | Physical realization, cyclic/closed comparison, global MC and recognition maps. |

Each assigned occurrence has `owner_group: 5`, `supplemental_assignment_id: CR-S05-P001`, and no prior owner in the frozen allocation. Both source records have `pdf: null`; therefore assigned PDF SHA-256 and physical pages are **not applicable**.

Both complete documents were exposed in source order:

- `R`: `[0,13530)`.
- `L`: `[0,4388)`.

Their raw snapshot-tree files and CAS aliases matched the same document hashes. No archived symlink was followed. Origin IDs are respectively:

- `R`: `4cec5d6a3167619d7a37c1eee2452e07e2a8c2b1ce099fedd3806e2cfb151512`.
- `L`: `3fec098739cf9b0fdc23aefaf3a3a5305576d56c423aa0e3e68c720b71ecae43`.

Required opening context `R:[0,8000)` matched `f71885060eda2ebeb92e3be958eb9eb0b7f57db792fe39034450c40434c75018`. `L`’s opening context is its complete document.

Additional recap context retains its existing owner, `coverage-0363`, from `semantic-reading/group-3.json`; no new coverage ownership is claimed:

| Context unit | Range read | SHA-256 |
|---|---|---|
| `R`, sequence 1 | `[2690,6831)` | `4267d94194f2669466cd0e716dc4a44e65c3199e4e454ee4ea153502242df43f` |
| `R`, sequence 2 | `[6831,9335)` | `14cb6af3e94b742e168ac75d18f2406416a94cf1100b589a6148ac58a3771ec8` |
| `R`, sequence 3 | `[9335,10805)` | `24265506df6b39348a0f29a690ca9ade3671b303d5884ce5236d133d801a33d6` |

Additional historical construction context:

- `P:102–176`, bytes `[7181,11075)`, SHA `436c06a6b5ab964c2398e26d74bc2fed8363749f1ad9432cd030f19b9d9abcd4`.
- `P:526–1123`, bytes `[22499,43414)`, SHA `c455c11f975cfb8fbd36200ce1463f80235b824bb580102e59ae245e0a5fd88a`.
- `P:1285–1327`, bytes `[51492,52745)`, SHA `7618027be6eeabfcf150423facf144a343105de3e974c49475ae945e4c89ab50`.
- `A:204–280`, `430–624`, and `1189–1207` were read. The latter two ranges are `[22815,34582)` and `[63179,65204)`. The first range’s byte endpoints were not separately recorded.
- These additional files were not found as matching hash-owned rows in the inspected named/supplemental inventory. Their ownership remains unresolved; this is context reading only.
- `P` and `A` were **not** read in full.

Additional live content read:

| File | Lines / byte intervals actually read |
|---|---|
| Volume-I integrated chapter | 550–615 / `[34926,38637)` |
| `holographic_datum_master.tex` | 3820–3920 / `[188360,193567)` |
| `part1_foundations.tex` | 1–80 / `[0,5557)` |
| `part2_duality.tex` | 245–325 / `[15007,19914)` |
| `part3_examples.tex` | 248–305 / `[10034,13126)` |
| `part4_physics.tex` | 1–78; 175–249 / `[10722,15316)`; 310–389 / `[18383,22168)` |
| Older `cy_to_chiral.tex` | 370–610 / `[34895,57379)`; truncated portions were reread explicitly |
| Integrated CY chapter | 1–160; 1230–1270 / `[80493,83905)` |
| Mixed-HT `main.tex` | 260–430 / `[11241,19494)` |
| Obstruction `paper.tex` | 1–205 / `[0,6563)`; 744–790 / `[25571,27324)` |

These sources retain their repository owners. Search hits outside these ranges are locators, not reading receipts.

Primary PDF checks:

- Current Engel PDF: 679,852 bytes, SHA `81ad7344e61d2c3e53a829a41c43161f1d64edfe2d2a534db898cf2231d65bc1`, 25 physical pages.
- Costello PDF: 477,083 bytes, SHA `75267b25c6b86c1be5616dd596bca354968cb12a3327d451ac6fd6b960e9015c`, 50 physical pages.
- Relevant extracted text was inspected. Screenshot requests for Engel physical pages 3, 5, 16, 17, 21 and Costello page 8 returned references without image payloads.
- **Physical pages visually inspected: none.** Neither external PDF was read in full. Neither has been identified byte-for-byte with the historical cited edition.

**Verification and remaining limits**

Read-only tools used: `cat`, `sed`, `rg`, Python standard-library hashing/JSON/integer arithmetic and memory-only URL reads, `git rev-parse`, `git status`, and web primary-source retrieval. Python reported version **3.14.6**, Clang **21.0.0**. The decisive matrix arithmetic used exact integers, exhaustive minors, and rational fractions; there were no floating-point error bounds to manage.

One inventory inspection initially assumed a dictionary where the JSON root was a list; it was corrected. One historical-source read had a mistyped hash path; the corrected path was subsequently read. No failure was treated as verification.

No tests, builds, filesystem renders, archived scripts, staging, commits, or pushes were run. No descendants were spawned. Required assigned text unread: **none**. Unresolved mathematical work remains exactly as recorded above, particularly the physical realization maps, closed-surface cyclic carrier, integral/parameter comparisons, and original-edition correspondence.
