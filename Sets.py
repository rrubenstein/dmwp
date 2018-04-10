import matplotlib.pyplot as plt
from sympy import FiniteSet
import random

def draw_venn(sets):
    venn2(subsets=sets)
    plt.show()

def make_set(lenth, range):
    s = []
    for i in range(0, lenth):
        x = random.randint(0, range+1)
        s.append(x)
    set = FiniteSet(*s)
    return set

def trial(num, min, max, prob):
    outcome = []
    expec = 0
    a = prob
    b = 0
    c = 0
    for i in range(0, num):
        x = random.randint(min, max)
        outcome.append(x)
        c = c + 1
    while a < 1:
        a = a + a
        b = b + 1
    for i in range(1, b):
        expec += i*prob
    mean = float(sum(outcome)/c)
    final = [expec, mean, num]
    return final

t1 = trial(100, 1, 6, 1/6)
t2 = trial(1000, 1, 6, 1/6)
t3 = trial(10000, 1, 6, 1/6)
t4 = trial(100000, 1, 6, 1/6)
t5 = trial(500000, 1, 6, 1/6)
tests = [t1, t2, t3, t4, t5]
print('Expected value: {0}'.format(t1[0]))
for test in tests:
    print('Trials: {0} Trial average: {1}'.format(test[1], test[2]))
