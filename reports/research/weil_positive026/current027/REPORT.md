# Arithmetic currents and prime inclusions

The candidate constructs an arithmetic current representation from the accepted native prime forms. It adds five proofs. All 39 inherited proofs and all five positive-weight proofs remain unchanged.

The reader module is `research-candidates/weil_positive026/current027/prime-current-carrier.tex`. Its SHA-256 is `3e8639041170fb59c6c76c2908c86ef4c131946f7096aed22a845ec188d2f3ce`. The five-file source aggregate is `a677f7c46a6ee524a3f70458112aae58ddbac01e5bedd10bc48dec79bb716eab`. The exact source manifest has SHA-256 `0c2826077bff987bbf311fcc509d763f22d49edec9fa42cd0ba5b92f9a36b6d8`.

This is a frozen construction candidate. It awaits independent mathematical acceptance. The verification scripts do not supply that acceptance.

## Mathematical result

For each prime, the construction retains every prime power with coefficient `(log p)p^(-m/2)`. The local Hilbert space is `H_p = L²(μ_p)`, where `μ_p` is the accepted positive Euler-factor measure. The arithmetic algebra is the algebraic direct sum of Schwartz functions over all primes. Its positive functional is integration over the disjoint union of the prime measure spaces. The GNS completion is `H = ⊕ H_p`.

The arithmetic algebra has no identity. Its extended positive weight has infinite mass, and its finite ideals are stated explicitly. The current algebra has a central identity operator. That identity does not supply a unit or a finite positive unitization for the arithmetic algebra.

On bosonic Fock space over `H`, creation, annihilation, and number currents preserve the dense domain of finite-particle vectors. Each particle sector is a completed Hilbert tensor space. Thus the common domain permits infinitely many prime coordinates within a particle sector. Creation and annihilation are unbounded for nonzero labels. The formulas give closable operators and explicit adjoint pairing identities. They do not identify restricted-domain operators with their complete Hilbert adjoints.

The current labels preserve complex linearity and the arithmetic involution. In pointwise notation, the decisive relations are

```
J+(b) = a*(b)
J−(b) = a(conj b)
N(b) = dΓ(M_b)
[J−(b), J+(d)] = ω(bd) I
[N(b), J±(d)] = ±J±(bd)
J±(b)† = J∓(b*)
```

For each finite prime set, the diagonal Fourier map is an injective convolution star homomorphism into the local arithmetic algebra. Pulling back the current labels gives `[A−(f), A+(h)] = W_P(f ⋆ h) I`. The current vectors have covariance `W_P(h* ⋆ f)`. The map from a test to its field current is linear and respects the involution. It is not an associative convolution homomorphism.

Prime inclusions insert zero coordinates. They preserve the weight, compose exactly, and induce Fock isometries that intertwine every local current. Their Hilbert completion is the full Fock space over `H`. Creation and annihilation extend to arbitrary square-summable prime vectors. Their cutoff limits converge on every finite-particle vector. Convergence on the vacuum forces square summability, so the criterion is exact for creation limits on a common domain containing the vacuum.

The native diagonal family `(hat f)_p` has finite `H` norm only for `f = 0` in ordinary `L²(du)`. Thus the cumulative native creation and field currents do not converge on the vacuum for any nonzero arithmetic test. This conclusion uses the accepted positive-form divergence theorem. It does not claim to exclude every distributional carrier or every domain that omits the vacuum.

The same native diagonal defines an actual bounded multiplication representation of the arithmetic algebra on `H`. Its second quantization defines a closed number current with an explicit maximal direct-sum domain. Finite-particle vectors form an invariant core. Self-adjoint tests give self-adjoint number currents. Prime cutoff number currents converge on this core and have the stated mixed relations with every square-summable creation label.

## Theorem obligations and anchors

| Obligation | Source anchor | Result |
|---|---|---|
| Native prime data and first deciding model | Lines 17–99, `eq:wc-local-data` through the occupation formulas | Both primes 2 and 3 retain all powers. Norms, cross pairings, two-particle products, and normalization are explicit. |
| Nonunital algebra, weight, finite ideals, Fourier map | Lines 103–191, `prop:wc-weight` | Proper arithmetic algebra and faithful multiplication GNS construction. |
| Operators, domains, products, and involution | Lines 193–370, `thm:wc-current` | Explicit contractions and sector bounds prove the current relations. |
| Compatible finite-prime system and true infinite extension | Lines 372–446, `thm:wc-system` | Exact inclusions and square-summable current domain. |
| Native diagonal obstruction | Lines 448–493, `prop:wc-diagonal-barrier` | No nonzero native diagonal creation vector or isometric identification preserving every test. |
| Infinite arithmetic multiplication and closed number currents | Lines 494–553, `prop:wc-infinite-multiplication` | Actual infinite representation, maximal operator domain, core, and mixed products. |
| Full-functional comparison | Lines 555–596, `eq:wc-weil-comparison` | Exact residual and obstruction to an orthogonal positive complement. |

## Deciding calculations

`check_currents.py` checks the two orthogonal Gaussian modes using an exact polynomial representation. It uses positive symbolic covariance parameters, complex labels, and bounded constant prime multipliers. All 28 input monomials of total degree at most six pass. Products use their full polynomial outputs, so no finite-dimensional CCR truncation is hidden.

The checks verify the central bilinear pairing, both mixed signs, the cross-prime commutator, adjoint pairings for the first-linear inner product, and the two-particle norm factors. Constant prime multipliers belong to the bounded multiplier extension. The two-mode subspace is not asserted to remain invariant under arbitrary Schwartz multipliers.

The script separately computes each full native Gaussian prime norm. It sums 360 prime powers and compares against Fourier integration of the rational Euler density. At `a = (log 2)²/8`, the norms are approximately `2.42024020453969426857` and `2.35928944234282174152`. The geometric remainder has an explicit analytic upper-bound formula. Its printed decimal value and the Fourier quadrature are diagnostics, not certified interval arithmetic. The maximum observed discrepancy is below `1.8 × 10^(-54)`.

The finite checks do not establish any infinite-prime limit. The manuscript supplies the proofs of the infinite representation and the obstruction.

## Primary-source evidence

Jan Dereziński, *Introduction to representations of the canonical commutation and anticommutation relations*, [arXiv:math-ph/0511030v2](https://arxiv.org/abs/math-ph/0511030v2), supplies the standard tensor-space conventions and current formulas. Section 2.2, preprint page 6, uses the inner product antilinear in its first argument. The candidate uses the opposite convention and adjusts every contraction and commutator pairing.

Sections 5.5–5.7, preprint pages 21–23, give second quantization, the Fock direct-sum relation, creation and annihilation, and the relevant commutators. Theorems 17 and 18 are the exact comparators for the CCR and mixed number-current relations. The manuscript proves the required formulas on its own weighted carrier and common domain. It does not transfer the arithmetic covariance or the infinite-prime conclusion from this reference.

The downloaded PDF is `primary-sources/derezinski-0511030v2.pdf`, with SHA-256 `696a733e17adf0abd4cf1824b8e9cb7def801e657f84143ea2487ad217d3e275`. Its extracted text is retained beside it. The original arithmetic coefficients, Fourier normalization, prime densities, GNS statements, divergence theorem, and Weil identity are consumed from the manifest-bound accepted dependencies.

## Failed routes and exact remaining boundary

An isometry between minimal finite-prime GNS spaces cannot identify the same arithmetic test across a strict prime extension. Its norm increases by a strictly positive new-prime form. The coherent inclusion instead retains each old prime coordinate and adds the new one as an orthogonal increment.

The cumulative native creation label fails the square-summability criterion. The vacuum therefore precludes convergence of those creation or field currents. The infinite multiplier and number-current construction remains valid because boundedness of a multiplier does not require finite weight.

The Fock vacuum does not represent the arithmetic functional. Number-current vacuum expectations vanish. Field-current products also fail multiplicativity as convolution observables. These facts prevent the construction from concealing the finite-mass obstruction.

The full Weil comparison remains unresolved. Its exact difference from the finite-prime covariance consists of the polar and archimedean terms, the diagonal subtraction `−2 C_P g(0)`, and the absolutely convergent omitted-prime tail. On every fixed nonzero convolution square this residual tends to negative infinity. Thus an orthogonal positive current sector cannot supply the residual for arbitrarily large cutoffs.

The next obligation is a construction that combines the prime, polar, and archimedean terms before defining its positive Hilbert covariance. It must use the same arithmetic test algebra and prove its actual product and domain comparison. No identification with another quantum current algebra, no root-space comparison, and no RH conclusion is claimed.

## Reproduction and custody

From this report directory, run:

```
/opt/homebrew/bin/python3 check_currents.py
/opt/homebrew/bin/python3 build_and_verify.py
```

The build script checks the source closure before compiling. It records three pdfLaTeX passes, environment overrides, the repeated PDF hashes, the `.fls` project inputs, and the render command. The final log must have no undefined reference, multiply defined label, box warning, package warning, or TeX error.

The reader contains 54 pages. Pages 1–45 match the accepted positive-weight reader in both extracted text and raster samples at scale 1.25. Pages 46–53 contain the current construction, and page 54 contains its primary bibliography. The visual inspection record is separate.

No writes occur outside the two assigned `current027/` directories. No staging, commit, push, central PDF copy, standalone PDF opening, integration, or publication occurs. No descendants were assigned.

The mathematical configuration requirement is `gpt-6-astra` with reasoning effort `ultra`. Independently observed runtime metadata was unavailable. The configuration gate remains unverified and was reported to the coordinator. No configuration mismatch was observed.

The final PDF SHA-256 is `37fbde897ab4a9db6aaf8d5d6eb08c67f40fc5cc9b17e3b483a51e23bb89d338`. All three final reproducible builds have identical PDF bytes. The final log is clean. Visual inspection of pages 45–54 found no remaining layout or manuscript-firewall defect.
