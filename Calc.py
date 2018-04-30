from sympy import Symbol, Derivative, sympify, pprint, solve, Integral, S, Limit, sin, cos, tan
from sympy.core.sympify import SympifyError

def derivative(f, var):
    var = Symbol(var)
    d = Derivative(f, var).doit()
    pprint(d)

def grad_ascent(x0, f1x, x):
    if not solve(f1x):
        print('oops')
        return
    epsilon = 1e-6
    step_size = 1e-4
    x_old = x0
    x_new = x_old + step_size*f1x.subs({x:x_old}).evalf()
    while abs(x_old - x_new) > epsilon:
        x_old = x_new
        x_new = x_old + step_size*f1x.subs({x:x_old}).evalf()
    return x_new

def cont_at(l, var, p):
    var = Symbol(var)
    try:
        pos_l = Limit(l, var, p).doit()
        neg_l = Limit(l, var, p, dir='-').doit()
    except Error:
        print('oops')
        return 2
    else:
        if pos_l == neg_l:
            return 1
        else:
            return 0

def verify_cont():
    f = raw_input('Enter a function in one variable: ')
    var = raw_input('Enter the variable: ')
    p = float(raw_input('Enter the point to check the continuity at: '))
    con = cont_at(f, var, p)
    if con == 1:
        print('{0} is continuous at {1}'.format(f, p))
    elif con == 2:
        print('{0} is not continuous at {1}'.format(f, p))
    else:
        print('didnt work')
