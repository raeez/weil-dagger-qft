"""Check the finite arithmetic identities and numerical Fourier conventions."""

from pathlib import Path
import json
import platform

import mpmath as mp
import sympy as sp


def check_equal(left, right):
    result = sp.factor(left - right)
    assert result == 0, result


x, r, z = sp.symbols("x r z", real=True)
matrix = sp.Matrix([[2 * (1 - x), 2 * x - 1 - x**4],
                    [2 * x - 1 - x**4, 2 * (1 - x)]])
check_equal(matrix[0, 0] + matrix[0, 1], 1 - x**4)
check_equal(matrix[0, 0] - matrix[0, 1], (1 - x)**2 * (x**2 + 2*x + 3))
check_equal(matrix.det(), (1 - x**4) * (1 - x)**2 * (x**2 + 2*x + 3))
geometric_difference = r/(1-r) - (r*z-r*r)/(1-2*r*z+r*r)
check_equal(geometric_difference,
            r*(1+r)*(1-z)/((1-r)*(1-2*r*z+r*r)))

# Compare the two finite prime-factor exponent counts without logarithmic numerics.
factorial_checks = []
for bound in [4, 5, 10, 31, 100]:
    expected = sp.factorint(sp.factorial(bound))
    actual = {}
    for prime in sp.primerange(2, bound + 1):
        power = prime
        while power <= bound:
            actual[prime] = actual.get(prime, 0) + bound // power
            power *= prime
    assert actual == expected
    factorial_checks.append(bound)

mp.mp.dps = 65
ell = mp.log(2)
a = ell**2/8
weight = ell/mp.sqrt(2)
gaussian = lambda u: mp.exp(-u*u/(4*a))/mp.sqrt(4*mp.pi*a)
square_gaussian = lambda u: mp.exp(-u*u/(8*a))/mp.sqrt(8*mp.pi*a)
f = lambda u: gaussian(u) + (2+1j)*gaussian(u-ell)
fhat = lambda t: mp.exp(-a*t*t)*(1+(2+1j)*mp.exp(1j*t*ell))
spatial = weight*mp.quad(lambda u: abs(f(u)-f(u-ell))**2,
                         [-mp.inf, -ell, 0, ell, 2*ell, 3*ell, mp.inf])
fourier = mp.quad(lambda t: abs(fhat(t))**2*weight*abs(1-mp.exp(1j*t*ell))**2,
                 [-mp.inf, -20, -10, 0, 10, 20, mp.inf])/(2*mp.pi)
coefficients = mp.matrix([1, 2+1j])
xx = mp.exp(-1)
gram = mp.matrix([[2*(1-xx), 2*xx-1-xx**4],
                  [2*xx-1-xx**4, 2*(1-xx)]])/mp.sqrt(2*mp.pi)
gram_value = (coefficients.transpose_conj()*gram*coefficients)[0]
assert abs(spatial-fourier) < mp.mpf('1e-50')
assert abs(spatial-gram_value) < mp.mpf('1e-50')
one_prime = weight*(2*square_gaussian(0)-2*square_gaussian(ell))
check_value = mp.sqrt(2/mp.pi)*(1-mp.exp(-1))
assert abs(one_prime-check_value) < mp.mpf('1e-60')

# Record the Gaussian mass ratio and its predicted leading coefficient.
mass_ratios = []
wc = lambda b: weight/mp.sqrt(mp.pi*b)*(1-mp.exp(-ell**2/(4*b)))
for exponent in [2, 3, 4, 5]:
    small = mp.mpf(10)**(-exponent)
    ratio = wc(small)**2/wc(2*small)
    leading = mp.sqrt(2)*weight/mp.sqrt(mp.pi*small)
    mass_ratios.append({'a': str(small), 'ratio': mp.nstr(ratio, 25),
                        'ratio_over_leading': mp.nstr(ratio/leading, 25)})

report = {
    'versions': {'python': platform.python_version(), 'sympy': sp.__version__,
                 'mpmath': mp.__version__},
    'exact_checks': {'prime_two_gram_eigenvalues': True,
                     'prime_two_gram_determinant': True,
                     'one_euler_factor_rational_density': True,
                     'factorial_prime_exponent_identity_bounds': factorial_checks},
    'numerical_check': {'digits': mp.mp.dps,
                        'spatial_difference_norm': mp.nstr(spatial, 55),
                        'fourier_density_integral': mp.nstr(fourier, 55),
                        'finite_gram_value': mp.nstr(gram_value, 55),
                        'spatial_fourier_difference': mp.nstr(abs(spatial-fourier), 8),
                        'spatial_gram_difference': mp.nstr(abs(spatial-gram_value), 8),
                        'scope': 'Diagnostic quadrature. Differences are observed errors, not certified error bounds.'},
    'mass_ratios': mass_ratios,
    'proof_scope': 'Symbolic identities certify only the displayed finite formulas. General positivity, domains, and divergence are proved in the TeX source.'
}
target = Path(__file__).with_name('calculation-results.json')
target.write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(report, indent=2))
