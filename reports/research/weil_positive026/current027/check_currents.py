"""Check prime current signs, products, and the two-prime Gaussian values."""

from pathlib import Path
import hashlib
import json
import platform

import mpmath as mp
import sympy as sp


out = Path(__file__).resolve().parent
x, y = sp.symbols("x y")
q2, q3 = sp.symbols("q2 q3", positive=True)
alpha = (1 + 2 * sp.I, 3 - sp.I)
beta = (2 - sp.I, -1 + 3 * sp.I)
eta = (2 + 5 * sp.I, -3 + sp.I)


def plus(label, polynomial):
    return sp.expand((label[0] * x + label[1] * y) * polynomial)


def minus(label, polynomial):
    return sp.expand(label[0] * q2 * sp.diff(polynomial, x)
                     + label[1] * q3 * sp.diff(polynomial, y))


def number(label, polynomial):
    return sp.expand(label[0] * x * sp.diff(polynomial, x)
                     + label[1] * y * sp.diff(polynomial, y))


def inner(left, right):
    left_terms = sp.Poly(left, x, y).as_dict()
    right_terms = sp.Poly(right, x, y).as_dict()
    value = 0
    for (r, s), coefficient in left_terms.items():
        value += (coefficient * sp.conjugate(right_terms.get((r, s), 0))
                  * sp.factorial(r) * sp.factorial(s) * q2**r * q3**s)
    return sp.expand(value)


def zero(value):
    assert sp.expand(value) == 0, value


basis = [x**r * y**s for r in range(7) for s in range(7-r)]
central = q2 * alpha[0] * beta[0] + q3 * alpha[1] * beta[1]
eta_alpha = tuple(eta[i] * alpha[i] for i in range(2))
for polynomial in basis:
    zero(minus(alpha, plus(beta, polynomial))
         - plus(beta, minus(alpha, polynomial)) - central * polynomial)
    zero(plus(alpha, plus(beta, polynomial))
         - plus(beta, plus(alpha, polynomial)))
    zero(minus(alpha, minus(beta, polynomial))
         - minus(beta, minus(alpha, polynomial)))
    zero(number(eta, plus(alpha, polynomial))
         - plus(alpha, number(eta, polynomial)) - plus(eta_alpha, polynomial))
    zero(number(eta, minus(alpha, polynomial))
         - minus(alpha, number(eta, polynomial)) + minus(eta_alpha, polynomial))
    zero(minus((1, 0), plus((0, 1), polynomial))
         - plus((0, 1), minus((1, 0), polynomial)))
    for other in basis:
        zero(inner(plus(alpha, polynomial), other)
             - inner(polynomial, minus(tuple(map(sp.conjugate, alpha)), other)))
        zero(inner(number(eta, polynomial), other)
             - inner(polynomial, number(tuple(map(sp.conjugate, eta)), other)))

zero(inner(plus((1, 0), plus((0, 1), 1)),
           plus((1, 0), plus((0, 1), 1))) - q2 * q3)
zero(inner(plus((1, 0), plus((1, 0), 1)),
           plus((1, 0), plus((1, 0), 1))) - 2 * q2**2)

# The polynomial representation has no particle truncation at the output.
# The largest input degree only bounds the finite exact calculation.
mp.mp.dps = 70
a = mp.log(2)**2 / 8
power_count = 360
prime_values = []
for prime in (2, 3):
    ell = mp.log(prime)
    rr = mp.mpf(prime)**(-mp.mpf(1)/2)
    prefactor = ell / mp.sqrt(2 * mp.pi * a)
    value = prefactor * mp.fsum(
        rr**m * (1-mp.exp(-m*m*ell*ell/(8*a)))
        for m in range(1, power_count+1))
    analytic_tail_bound = prefactor * rr**(power_count+1)/(1-rr)

    def density(t):
        return (2 * ell * rr * (1+rr) * (1-mp.cos(t*ell))
                / ((1-rr)*(1-2*rr*mp.cos(t*ell)+rr*rr)))

    integral = mp.quad(lambda t: mp.exp(-2*a*t*t)*density(t),
                       [-mp.inf, -60, -30, -15, -7, 0, 7, 15, 30, 60, mp.inf])
    integral /= 2 * mp.pi
    assert abs(integral-value) < mp.mpf("1e-45")
    prime_values.append({
        "prime": prime,
        "a": mp.nstr(a, 65),
        "powers_summed": power_count,
        "sum": mp.nstr(value, 60),
        "analytic_truncation_upper_bound": mp.nstr(analytic_tail_bound, 12),
        "fourier_quadrature": mp.nstr(integral, 60),
        "observed_difference": mp.nstr(abs(value-integral), 12),
    })

result = {
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "versions": {"python": platform.python_version(), "sympy": sp.__version__,
                 "mpmath": mp.__version__},
    "exact_checks": {
        "monomials_through_total_degree": 6,
        "input_monomial_count": len(basis),
        "complex_coefficients": [list(map(str, item)) for item in (alpha, beta, eta)],
        "bilinear_central_pairing": str(central),
        "creation_annihilation_commutators": True,
        "mixed_number_commutator_signs": True,
        "cross_prime_commutation": True,
        "first_linear_adjoint_pairings": True,
        "two_particle_norm_factors": True,
    },
    "gaussian_values": prime_values,
    "calculation_scope": (
        "Exact symbolic identities check two orthogonal prime Gaussian modes, "
        "including complex labels and bounded constant multipliers. The "
        "finite-mode space is not invariant under arbitrary Schwartz multipliers. "
        "The manuscript proves those full operator relations separately. "
        "The analytic series-tail bound is rigorous as a formula. Its printed "
        "decimal evaluation and the quadrature are numerical diagnostics, "
        "not certified interval arithmetic. No finite calculation proves "
        "an infinite-prime limit or the full Weil comparison."
    ),
}
(out / "calculation-results.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
