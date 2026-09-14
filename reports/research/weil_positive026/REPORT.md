# Positive prime translation forms

The construction produces an unconditional positive nonunital arithmetic carrier. It keeps the exact Weil prime-power coefficients on each finite cutoff and on every power of a fixed prime. Positivity requires an explicit diagonal compensation. The compensation prevents this construction from being a factorization of the full Weil functional.

The additive mathematical source is `research-candidates/weil_positive026/prime-difference-carrier.tex`. Its frozen SHA-256 is `00338ca975438f5a457354e13f808d1245830da49888edf92c9e633b43bcfc6b`. The source closure and exact reader diff appear in `source-manifest.json` and `source.patch`.

The source supplies five complete proofs, an exact Gaussian calculation, and an exact two-dimensional arithmetic Gram matrix. The proofs establish the result only within the boundary stated below. Independent mathematical acceptance remains required.

## Ground truth and preservation

The packet named a nonexistent synthesis032 worktree. The corrected live source is the arithmetic chapter preserved inside the synthesis033 worktree. Its three copies in `programme-032`, `programme-033/immutable032`, and `programme-033/source` were independently compared. All have SHA-256 `56b73a14e153c3405d29e9b842919d6576cff110d17175a2e999443745d17112`, 3,129 lines, and 39 proof environments.

The full chapter was read before construction. Its unchanged bytes are in `inputs/arithmetic.tex`. Every existing proof is preserved. The new module requires no edits to that chapter. The complete 38-page inherited arithmetic rendering is text-identical and pixel-identical to the first 38 pages of the 45-page candidate rendering. Each comparison is recorded in `verification-results.json`.

The native source snapshot is `inputs/native-paper.tex`, SHA-256 `1902189145183342a560527ba18e54cdbb443054523bff29b1945f1490abb799`. It contains the normalized Weil functional, the conditional nonunital GNS construction, and the independent arithmetic question. The fuller arithmetic chapter supplies the subsequently proved finite-mass obstruction and exact common-domain results. The native source remains unmodified.

No archive assertion was used as evidence. No zero location was used to define a measure, Hilbert space, generator, or positivity assumption. A background literature search did not enter the proof dependencies. No novelty or priority claim is made.

## Mathematical target and outcome

The intended full question is to construct a positive functional on a proper nonunital arithmetic or current algebra and a star homomorphism whose pullback is the full Weil functional. The construction must derive positivity independently of RH. This full question remains unresolved.

The proved boundary is a native arithmetic local construction, together with a precise obstruction to its direct global extension:

| Claim | Exact source anchor | Proof or deciding calculation |
| --- | --- | --- |
| Prime 2 gives a positive translation-difference form with the exact coefficient `log(2)/sqrt(2)` | `ex:wp-prime-two`, lines 28–83 | The raw prime term is negative on the chosen Gaussian square. Adding the diagonal term gives `sqrt(2/pi)(1-exp(-1))`. The two-vector Gram eigenvalues factor exactly. |
| For nonzero summable nonnegative coefficients, the positive form is the Fourier integral against the explicit nonnegative density | `thm:wp-positive-form`, line 108 | Fourier inversion and the spatial square identity prove equality. The density is positive almost everywhere. |
| The least diagonal compensation is exactly twice the coefficient sum | `thm:wp-positive-form`, line 108 | Broad Gaussians force the lower bound. The translation-difference identity proves sufficiency. |
| Every power of one fixed prime is included by a convergent geometric series | `eq:wp-euler-density`, lines 158–177 | The explicit rational Fourier density is nonnegative. The weight and all off-diagonal coefficients retain the native exponent one-half. |
| The Fourier map gives a nonunital Schwartz-algebra realization with an infinite positive weight | `thm:wp-carrier`, line 204 | Positivity, zero null space, image density, bounded multiplier norms, and failure of finite unit mass are proved. |
| The real frequency coordinate is an unbounded self-adjoint multiplier with an explicit invariant domain for every polynomial product | `prop:wp-domain`, line 324 | The maximal multiplication domain and all-moment intersection are specified. Adjoints, cores, graph completeness, and image density are proved directly. |
| The all-prime positive sum converges for exponent greater than one and diverges on every nonzero ordinary L2 vector for exponent at most one | `thm:wp-prime-limit`, line 412 | The factorial divisor identity proves coefficient divergence. Decay of translation correlations proves the form divergence. No prime number theorem is required. |
| Exact subtraction recovers the native prime distribution but loses positivity | `prop:wp-native-comparison`, line 489 | All polar, gamma, prime, and diagonal terms appear with explicit signs. The remaining residual becomes negative on each fixed nonzero square as the cutoff grows. |

All spaces are over the usual complex field, in degree zero. All real measures, Fourier signs, domains, and topologies appear in the source. No formal coefficient specialization is used.

## Comparison map and missing edge

The constructed map is the Fourier star homomorphism from the existing Weil convolution algebra into the pointwise Schwartz algebra. The positive functional is integration against the independently defined density `sum c_n |1-exp(i t log n)|^2 dt/(2 pi)`. Its exact pullback is the compensated prime functional `W_c`.

This map realizes the native negative prime coefficients. It also adds the necessary term `2 C g(0)`. The finite-mass obstruction holds for this carrier because its Gaussian mass ratio diverges as a constant times `a^(-1/2)`. The full Weil ratio has an additional logarithm. In particular, the ratio `W_c(g_a)/L_zeta(g_a)` tends to zero for each fixed summable coefficient family.

For native finite cutoffs, the exact residual is the polar and archimedean functional minus `2 C_X g(0)` and minus the remaining prime tail. Its value tends to minus infinity on every fixed nonzero convolution square. Thus it cannot be supplied by an independently positive correction at every sufficiently large cutoff.

The missing edge is a jointly positive realization of all three full arithmetic terms after the divergent diagonal cancellation. It must preserve convolution and the involution. A quantum-current interpretation additionally needs an actual map identifying products and adjoints on a common invariant domain. Neither comparison is constructed here.

## Failed routes and their status

1. Summing the positive native prime-difference forms directly over all primes is refuted. The increasing limit has finite domain `{0}` on ordinary `L2(R)`.
2. Lowering the diagonal compensation while preserving the native off-diagonal coefficients is refuted for every summable positive family. Positivity holds exactly when the diagonal coefficient is at least `2 C`.
3. Subtracting the diagonal term and retaining positivity is refuted. The resulting prime functional is strictly negative on every Gaussian convolution square.
4. Adding a positive polar/archimedean residual to each large native cutoff is refuted. The residual is negative on each fixed nonzero square once the cutoff is large enough.
5. Continuing the damped Dirichlet-series expression does not continue its positive sum. The positive form already loses every nonzero finite vector at exponent one.
6. A joint construction after cancellation remains unresolved. The deciding next step is an actual norm identity for the full local expression, with no premise equivalent to Weil positivity.

These failures concern the specified methods. They do not refute full Weil positivity.

## Calculation and build evidence

Run from `reports/research/weil_positive026`:

```sh
/opt/homebrew/bin/python3 calculate.py
/opt/homebrew/bin/python3 verify.py
TEXINPUTS=./inputs: pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build-baseline baseline.tex
TEXINPUTS=./inputs: pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build-candidate candidate.tex
```

Run each LaTeX command until its references stabilize. The baseline used three passes. The final candidate bytes received two convergent passes after the last source edit. The final logs contain no warnings, undefined references, duplicate labels, or overfull/underfull boxes.

The calculation uses Python 3.14.6, SymPy 1.14.0, and mpmath 1.3.0. Exact symbolic checks verify the two-vector Gram eigenvalues and determinant, the one-prime geometric density, and finite factorial prime-exponent identities. A separate spatial integral, Fourier integral, and finite Gram expression agree for a complex linear combination at 65-digit precision. The numerical differences are diagnostics without certified quadrature error bounds. They do not establish the general theorems.

The source manifest supplies every mathematical dependency hash and the aggregate source diff hash. The complete dependency closure is the new module, the unchanged arithmetic chapter, the unchanged shared template, and the candidate harness. The harness uses the existing template without local typography changes.

The initial baseline invocation used an incorrect repeated relative directory prefix. It failed before writing a manuscript or running LaTeX. The corrected invocation and all final builds succeeded. One early candidate had an underfull heading, and two statements split across pages. The source corrected these layout defects before its freeze.

The candidate PDF is an internal QA artifact. It has 45 pages, with the addition on pages 39–45. Its SHA-256 is `9115251c8df79a8f0d4394904b8851b6e24cb44248cab96ad9b1d7663e449142`. Every font is embedded, subset, and accompanied by Unicode mapping. All changed pages and the preceding transition were visually inspected. The final two pages were inspected again after the last pagination change. No standalone PDF was opened in a desktop application or published.

## Integration and custody

The preferred include location is directly after the complete arithmetic-forms chapter and before the prime-distribution continuation. The dependency labels appear in `source-manifest.json`. They all resolve inside the exact inherited arithmetic chapter. The new module introduces no colliding labels.

The only writable scopes used are `research-candidates/weil_positive026/` and `reports/research/weil_positive026/` in the assigned worktree. No existing tracked file was changed. No staging, commit, push, cleanup, publication, or external message occurred.

Required runtime controls and their observation limits are recorded in `source-freeze.json`. This construction does not self-certify mathematical acceptance. The coordinator owns the independent acceptance and any successor-reader integration.
