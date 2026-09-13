"""Exact algebraic checks for the domain and Gaussian calculations.

These identities check the specified symbolic expressions. Summability,
closedness, asymptotic remainders, and arithmetic positivity require the
proofs and hypotheses in paper.tex.
"""
import json
import platform
import sympy as s

n = s.symbols("n", integer=True, positive=True)
a = s.symbols("a", positive=True)
u, v = s.symbols("u v", real=True)
ga = s.exp(-u**2/(4*a)) / s.sqrt(4*s.pi*a)
convolution = s.integrate(
    s.exp(-(v**2 + (u-v)**2)/(4*a))/(4*s.pi*a),
    (v, -s.oo, s.oo),
)
assert s.simplify(convolution - ga.subs(a, 2*a)) == 0
constant = 1/(4*s.sqrt(s.pi))
leading = constant*a**s.Rational(-1, 2)*s.log(1/a)
ratio = leading**2/leading.subs(a, 2*a)
ratio_coefficient = s.limit(ratio/(a**s.Rational(-1, 2)*s.log(1/a)), a, 0)
assert ratio_coefficient == s.sqrt(2)/(4*s.sqrt(s.pi))
gaussian_gram = s.Matrix([[1/s.sqrt(2), 1/s.sqrt(5)],
                          [1/s.sqrt(5), 1/s.sqrt(8)]])
assert gaussian_gram.det() == s.Rational(1, 20)
assert s.simplify(n**2*(n**-2)**2) == n**-2
assert s.simplify(n**4*(n**-2)**2) == 1
weighted_vector = s.exp(n/2)/n
assert s.simplify(s.exp(-n)*weighted_vector**2) == n**-2
assert s.simplify(s.exp(-n)*n**2*weighted_vector**2) == 1
J = s.diag(1, -1)
X = s.Matrix([[0, 0], [1, 0]])
indefinite_square = (J*(J*X.T*J)*X)[0, 0]
assert indefinite_square == -1
z, lam = s.symbols("z lambda")
assert s.expand((z*s.eye(2)-lam*s.eye(2)).det() - (z-lam)**2) == 0
print(json.dumps({
    "python": platform.python_version(),
    "sympy": s.__version__,
    "gaussian_convolution": "g_a * g_a = g_(2a)",
    "gaussian_leading_coefficient": str(constant),
    "unitization_ratio_coefficient": str(ratio_coefficient),
    "two_scale_gaussian_gram_determinant": str(gaussian_gram.det()),
    "maximal_domain_terms": ["n^(-2)", "1"],
    "target_domain_terms": ["n^(-2)", "1"],
    "indefinite_square": str(indefinite_square),
    "multiplicity_example": ["s-lambda", "(s-lambda)^2"],
    "scope": "Exact symbolic identities only; no numerical or general theorem acceptance."
}, indent=2))
