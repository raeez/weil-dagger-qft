from pathlib import Path
import json
import sys
import sympy as s

R = Path(__file__).resolve().parent
I = s.I
results = {}
def unit(n, i, j):
    a = s.zeros(n)
    a[i, j] = 1
    return a
n = 4
for i in range(n):
    for j in range(n):
        assert unit(n, i, j).H == unit(n, j, i)
        for k in range(n):
            for ell in range(n):
                assert unit(n, i, j) * unit(n, k, ell) == (unit(n, i, ell) if j == k else s.zeros(n))
results['matrix_unit_identities'] = {'dimension': n, 'product_checks': n ** 4, 'adjoint_checks': n ** 2}

variables = s.symbols('a0:4 b0:4', real=True)
A = s.Matrix(2, 2, lambda i, j: variables[2*i+j] + I*variables[4+2*i+j])
assert s.expand(s.trace(A.H * A)) == sum(x*x for x in variables)
test = s.Matrix([[1, I], [2, 0]])
left = s.kronecker_product(s.eye(2), test)
assert (test.H * test).eigenvals() == {3 - s.sqrt(5): 1, 3 + s.sqrt(5): 1}
assert (left.H * left).eigenvals() == {3 - s.sqrt(5): 2, 3 + s.sqrt(5): 2}
results['symbolic_trace_norm'] = {'trace_square': str(s.expand(s.trace(A.H * A))),
    'operator_norm_squared': str(3+s.sqrt(5)), 'left_action_norm_squared': str(3+s.sqrt(5))}
c = s.symbols('c', real=True)
rows = []
for n in range(1, 9):
    q = s.diag(*([1]*n + [0]))
    assert s.trace(q) == n and q*q == q and q.H == q
    rows.append({'rank': n, 'unit_complement_mass': str(c-n), 'mass_bound_ratio': n})
results['finite_corner_obstruction'] = rows
results['general_scope'] = 'The manuscript uses every positive integer n, so c >= n has no finite solution. The finite computations do not prove this quantifier by themselves.'

u, h = s.symbols('u h', real=True)
hp = s.symbols('hp', positive=True)
def gauss_polynomial(p):
    d = s.Poly(p, u).degree()
    if d is s.S.NegativeInfinity:
        return s.S.Zero
    return s.expand(sum(h**m * s.diff(p, u, 2*m).subs(u, 0) / (2**m*s.factorial(m)) for m in range(int(d)//2+1)))
moments = []
for k in range(11):
    integral = s.integrate(u**k * s.exp(-u*u/(2*hp)), (u, -s.oo, s.oo))/s.sqrt(2*s.pi*hp)
    formula = gauss_polynomial(u**k).subs(h, hp)
    assert s.simplify(formula-integral) == 0
    moments.append({'degree': k, 'moment': str(formula)})
p = (1+I*u+u**6) + h*(u**3-2*u**4) + h**2*(3+u**8)
assert s.expand(gauss_polynomial((1+2*h-h**3)*p) - (1+2*h-h**3)*gauss_polynomial(p)) == 0
results['gaussian_moments'] = moments
results['formal_module_linearity_polynomial_residual'] = '0'
v = s.symbols('v')
inverse = sum((h/v)**j for j in range(10))
assert s.expand((1-h/v)*inverse - (1-(h/v)**10)) == 0
results['formal_inverse_residual_through_order9'] = '0'
results['formal_specialization_scope'] = 'For nonzero v, 1-hbar/v is a unit in the full formal ring. A unital C-algebra homomorphism cannot send this unit to zero. Evaluation at zero exists.'

a = s.symbols('a', positive=True)
g = s.exp(-u*u/(4*a))/s.sqrt(4*s.pi*a)
assert s.simplify((-u*g) - (u*g).subs(u, -u)) == 0
assert s.simplify((s.exp(-u*u/(8*a))/s.sqrt(8*s.pi*a)).subs(u, 0) - g.subs(u, 0)) != 0
results['gaussian_map_obstructions'] = {'involution': 'J(u)^* = -J(u)', 'product': 'g_a star g_a = g_2a != g_a'}

x, y = s.symbols('x y')
def bracket(f, g):
    return s.diff(f, x)*s.diff(g, y) - s.diff(f, y)*s.diff(g, x)
monomials = [x**i*y**j for degree in range(1, 5) for i in range(degree+1) for j in [degree-i]]
checks = 0
for f in monomials:
    for g0 in monomials:
        for probe in [x, y]:
            assert s.expand(bracket(f, bracket(g0, probe)) - bracket(g0, bracket(f, probe)) - bracket(bracket(f, g0), probe)) == 0
            checks += 1
results['hamiltonian_representation'] = {'monomials_each_input': len(monomials), 'coefficient_checks': checks,
    'row_domain': 'Output through degree N uses only input monomials through N+1 in each nonconstant input.'}

t = s.symbols('t', real=True)
assert s.trigsimp(3+4*s.cos(t)+s.cos(2*t)-2*(1+s.cos(t))**2) == 0
M = s.Matrix([[1/s.sqrt(2), 1/s.sqrt(5)], [1/s.sqrt(5), 1/s.sqrt(8)]])
assert s.det(M) == s.Rational(1, 20)
lead = 1/(4*s.sqrt(s.pi))
assert s.simplify(lead**2/(lead/s.sqrt(2))-s.sqrt(2)/(4*s.sqrt(s.pi))) == 0
assert s.simplify(-I*s.diff(s.exp(-x), x)-I*s.exp(-x)) == 0
assert s.simplify(-I*s.diff(s.exp(x), x)+I*s.exp(x)) == 0
results['inherited_decisive_constants'] = {'boundary_trig_residual': '0', 'minimal_zero_exponent': 1,
    'gaussian_gram_determinant': '1/20', 'weil_mass_ratio_coefficient': str(s.sqrt(2)/(4*s.sqrt(s.pi))),
    'half_line_deficiency_generators': ['exp(-x) square integrable', 'exp(x) not square integrable']}
results['versions'] = {'python': sys.version, 'sympy': s.__version__}
results['error_bounds'] = 'Exact symbolic arithmetic. No approximate numerical conclusions.'
(R / 'independent-calculations.json').write_text(json.dumps(results, indent=2) + '\n')
print('All independent exact calculations passed.')
