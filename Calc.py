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

def grad_decent(x0, f1x, x):
    epsilon = 1e-6
    step_size = 1e-4
    x_old = x0
    x_new = x_old - step_size*f1x.subs({x:x_old}).evalf()
    while abs(x_old + x_new) > epsilon:
        x_old = x_new
        x_new = x_old - step_size*f1x.subs({x:x_old}).evalf()
    return x_new

def gradiant():
    f = raw_input('Enter a function in one variable: ')
    var = raw_input('Enter the variable to differentiate with respect to: ')
    var0 = float(raw_input('Enter the initial value of the variable: '))
    try:
        f = sympify(f)
    except SympifyError:
        print('oops')
    else:
        var = Symbol(var)
        d = Derivative(f, var).doit()
        var_min = grad_decent(var0, d, var)
        print('{0}: {1}'.format(var.name, var_min))
        print('Minimum value: {0}'.format(f.subs({var:var_min})))

def intergal_of_curve(f, var, start, finish):
    var = Symbol(var)
    integ = Integral(f, (var, start, finish)).doit()
    return integ

def area_bet_curve():
    f1 = raw_input('Enter the upper function: ')
    f2 = raw_input('Enter the lower function: ')
    var = raw_input('Enter the variable: ')
    a = float(raw_input('Enter the starting point: '))
    b = float(raw_input('Enter the ending point: '))
    fx1 = intergal_of_curve(f1, var, a, b)
    fx2 = intergal_of_curve(f2, var, a, b)
    area = fx1 - fx2
    print('The area between the functions {0} and {1} between {2} and {3} is {4}'.format(f1, f2, a, b, area))

def len_of_arc(f, var, start, finish):
    var = Symbol(var)
    d = Derivative(f, var).doit().evalf()
    f1 = (1 + (d)**2)**0.5
    integ = Integral(f1, (var, start, finish)).doit().evalf()
    return integ

def find_length_arc():
    f = raw_input('Enter the function: ')
    var = raw_input('Enter the variable: ')
    a = float(raw_input('Enter the starting point: '))
    b = float(raw_input('Enter the ending point: '))
    f = sympify(f)
    c = len_of_arc(f, var, a, b)
    c = sympify(c)
    print('The length of {0} between {1} and {2} is {3}'.format(f, a, b, c))

find_length_arc()
