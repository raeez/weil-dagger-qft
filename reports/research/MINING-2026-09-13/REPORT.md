# Weil source construction and exact review boundary

Status: implemented, built, visually inspected, and frozen for independent review. No mathematical acceptance, integration, commit, push, or publication is asserted.

The principal checkout was clean at `cce2bc383bcf2fd930e917a5abb773e0469465cc` on `main`. The candidate uses `/Users/raeez/mathematics/worktrees/frontier-mine-weil-20260913`, branch `repair/frontier-mine-weil-20260913`. Only `paper.tex`, `README.md`, and this report tree were changed. Requested mathematical controls are `gpt-6-astra` and `ultra`; separately observed runtime metadata is unavailable and remains unverified. No children were created.

## Mathematical spine

The question is whether the arithmetic local terms define a positive pairing independently of RH. A positive pairing gives a nonunital GNS representation, whose common graph completion must preserve all algebra products. A finite vector representing the functional is a stronger requirement.

The source constructs that common domain and proves its precise transfer theorem. It also reconstructs a previously unconsumed local Gaussian obstruction, then derives positive finite Gaussian subspaces. The independent arithmetic positivity problem remains open.

The main source anchors are:

- `thm:graph-domain`: the graph completion is the intersection of every multiplier closure domain. The estimate for `c = sum a* a` proves simultaneous approximation. Applying all products to the approximating net proves invariance, the adjoint pairing, continuity, and minimality.
- `ex:maximal-domain`: for `N e_n = n e_n`, the vector `v_n = n^-2` belongs to the maximal form domain of `||N v||²`, but `N v` does not. The all-moment domain is invariant.
- `prop:graph-transfer`: the GNS isometry identifies the completed representation of the image algebra in its closed Hilbert range. Ambient closures give inclusion. Surjectivity of the algebra map gives full graph-domain equality.
- `ex:transfer-domain`: `c00` inside `C[n]+c00`, with the positive weight `e^-n`, gives an onto Hilbert isometry that does not carry the source's full domain into the larger target algebra's common domain.
- `thm:weil-mass`: `L_zeta(g_a) = a^-1/2 log(1/a)/(4 sqrt(pi)) + O(a^-1/2)`. The polar term is bounded, the prime term has an explicit exponential bound, and the real-frequency gamma integral supplies the leading coefficient. No zeros or RH enter the proof.
- `thm:gaussian-subspaces`: any fixed finite family of distinct positive scales gives a positive definite Weil Gram matrix at all sufficiently small common scales. Its normalized limit has entries `(lambda_j+lambda_k)^-1/2`, the Gram matrix of independent Gaussians. The two-scale determinant is `1/20`.
- `cor:weil-carriers`: no finite positive unitization, finite-norm vector realization on an invariant representation domain, or positive-functional pullback from a C*-algebra exists for the full functional.
- Section 7 preserves the unconditional Hermitian radical quotient and its left convolution action. Its positive Hilbert completion remains conditional on positivity. The final paragraph preserves the trace-multiplicity counterexample.

## Recovered arguments and failed routes

`mining-dispositions.json` records exact source hashes, byte and line anchors, snapshots, dispositions, destination labels, and residual obligations. It includes the current source, the full synthesis GNS arguments, recent complete returns, visible intermediate public statements from their sessions, the original project seed, the historical pre-Krein construction, and relevant earlier Gaussian/KMS/co-Poisson passages. Missing private or unsaved reasoning is not reconstructed. This bounded source phase does not certify whole-corpus coverage.

Several recovered claims require separate handling:

1. The zero-product algebra `A=Cx`, `x*=x`, `x²=0`, `L(x)=1` has a nonzero square-positive Hermitian functional and zero GNS Hilbert space. This valid example is retained here; the paper proves the stronger obstruction for the actual Weil functional.
2. In the archived KMS formula, `mu_m* mu_m=1` conflicts with `phi(mu_m* mu_m)=1/m` and `phi(1)=1`. The defining functional does not exist as written. This is a direct relation check, independent of a KMS theorem. The Volume IV owner must construct a consistent state and its domains. Even a consistent C*-state cannot pull back to the full Weil functional.
3. The archived balanced Gaussian functional includes the negative zero sum. Its asserted value zero is an explicit-formula identity, not positivity of the arithmetic functional. Its Gaussian convolution calculation survives after normalization. The inconsistent Fourier/prime/gamma carrier is not imported. The paper uses an absolutely convergent gamma integral and proves a positive finite-family result.
4. The archived co-Poisson condition CP1 requires both `phi(0)>0` and an ordinary zero mean `integral_0^infinity phi(y) dy/y=0`, with `phi` an autocorrelation. For nonzero `f` in `L²`, translations are strongly continuous, so `phi` is continuous and `phi(0)=||f||²`. Hence `Re(phi(y))>||f||²/2` near zero and the logarithmic integral diverges. This refutes the stated ordinary-integral domain. A subtracted or regularized mean would require a new definition, its cutoff dependence, and a new comparison theorem. CP3 separately assumes the intended inequality. No nonemptiness or positivity is inferred from it.
5. The rank-one Hilbert-Schmidt range counterexample is retained in the ledger. Finite matrix support gives a dense range, whereas arbitrary finite rank does not. Its consumer belongs to Volume IV.
6. The full-domain Deninger implication remains a valid conditional argument. It constructs no arithmetic operator, determinant, or spectral multiplicity comparison. The final finite example explains why equal functionals cannot supply that comparison.

## Verification

The unchanged baseline was rebuilt before edits. The final command is `SOURCE_DATE_EPOCH=1788515194 make check`. It performs two LaTeX passes. A forced repeat with `make -B check` produced an identical PDF, as recorded in `reproducibility.json`.

The final PDF has 13 pages. All 13 page images were visually inspected. The last wording pass changed only pages 4 and 8; their PNG hashes identified these changes, and both pages were inspected again. Equations, domains, exponents, page transitions, and references are legible. No clipping or overlap was observed. The final LaTeX log contains no warnings, undefined references, duplicate labels, overfull boxes, or underfull boxes. `git diff --check` passes.

The manuscript source and extracted PDF text have zero hits for the specified project-management, closed-repository-path, and prohibited prose patterns. PDF metadata contain mathematical content only. These checks support the direct source and visual inspection; they do not certify the mathematics.

`check_calculations.py` ran with `/opt/homebrew/opt/python@3.14/bin/python3.14` and SymPy 1.14.0. It independently checks Gaussian convolution, the asymptotic ratio coefficient, the two-scale Gram determinant, both domain example terms, the indefinite square, and the finite determinant multiplicity. Its output is in `calculations.json`. These are exact symbolic identities, not numerical evidence or a general theorem certificate.

Two verification failures were resolved. The worktree's default `python3` lacked SymPy, so the existing Python 3.14 environment was selected explicitly. One determinant assertion compared expanded and factored symbolic expressions structurally; subtraction and expansion verifies their equality. No mathematical formula changed in response to that assertion failure.

Primary checks: DLMF equation 5.11.2 and its sector condition were read directly. The equation source is retained. Powers's primary preprint was retrieved from OSTI, and Definition 2.4 plus Lemmas 2.5–2.6 were read; physical pages 9–10 were visually inspected. These agree with the graph-domain construction, whose proof here also handles the nonunital case. Original Weil and Segal scans were not newly retrieved in this phase. Their existing theorem locators remain a required source-review check; no fresh source acceptance is claimed for them.

## Remaining obligations

Independent lanes must review the identical `freeze.json` candidate, especially simultaneous graph approximation, closure-domain variance, the local Gaussian remainder, finite-family quantifier order, and the whole-paper arithmetic source normalization. The exact independent positivity problem is unresolved. No threshold uniform over all Gaussian families is proved. No self-adjoint arithmetic generator, vacuum state, reflection-positive QFT, positive weight, or determinant bridge is constructed.

The parent owns propagation to the synthesis arithmetic module, Volume IV, and the Deninger paper. No consumer was edited here. The central accepted PDF remains untouched.
