# The Zeta–Weil Form and Nonunital GNS Transfer

This paper fixes the Fourier, involution, measure, polar,
archimedean, and prime-power conventions for the full zeta--Weil functional
on a concrete nonunital convolution $*$-algebra.  Its arithmetic statement is
Weil's exact criterion
\[
  \mathrm{RH}\quad\Longleftrightarrow\quad
  L_\zeta(f^*\star f)\geq 0\qquad\text{for every }f\in\mathcal A_\zeta.
\]
Thus Weil positivity is equivalent to the Riemann hypothesis; it is not an
independent proof of it.

The paper proves the nonunital algebraic GNS construction, automatic
closability of its multipliers, and the exact boundedness criterion.
The common graph completion is the intersection of all multiplier closure
domains.  A sum-of-squares estimate proves simultaneous approximation and
invariance under every algebra product.  Positive-functional pullback
identifies the closed representation of the image algebra.  An explicit
example shows why it need not identify the full target algebra's domain.

A Gaussian calculation using the arithmetic local terms proves
\[
 L_\zeta(g_a)=\frac{a^{-1/2}\log(1/a)}{4\sqrt\pi}+O(a^{-1/2}),
 \qquad \widehat g_a(t)=e^{-at^2}.
\]
It follows that the full Weil functional has no finite-mass positive
unitization.  This excludes both a finite-norm representing vector on an
invariant representation domain and a pullback from a positive functional
on a $C^*$-algebra.  The obstruction is unconditional.  Under RH the GNS
convolution multipliers are nevertheless bounded.

The same asymptotic constructs positive Gaussian subspaces of every fixed
finite dimension.  For distinct positive scales $\lambda_j$, the normalized
Gram matrix tends to $((\lambda_j+\lambda_k)^{-1/2})$, a positive-definite
Gaussian integral matrix.  The required small-scale threshold depends on
the finite family; this does not prove positivity on the whole test algebra.

For general nonunital $C^*$-algebras, the paper gives the sharp positive
unitization criterion and the approximate-identity construction of the
minimal cyclic vector.

Explicit examples delimit these conclusions: a symmetric closable operator
need not have a self-adjoint extension, algebraic positive unitization can
fail, the isotropic cone of an indefinite form is not a quotient subspace,
and a radical quotient alone does not produce a Krein space or positivity.
Accordingly, no theorem passing from bare pre-Krein data to a positive GNS
representation is asserted.
The remaining arithmetic problem is an independent positive functional
on a suitable test algebra, without using RH, the zeta zeros, or equivalent
Weil positivity.  Its finite-mass unitization must fail.  A determinant
interpretation also needs a separate comparison of spectral multiplicities.

Build with `make check`.
