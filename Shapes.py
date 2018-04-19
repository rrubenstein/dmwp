from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib import cm as cm 
import math
import random

def create_circle(r):
    if r == None:
        r = 0.05
    circle = plt.Circle((0,0), r)
    return circle

def update_radius(i, circle):
    circle.radius = i*0.5
    return circle,

def create_animation_grow():
    fig = plt.gcf()
    ax = plt.axes(xlim=(-10, 10), ylim=(-10, 10))
    ax.set_aspect('equal')
    circle = create_circle(0.05)
    ax.add_patch(circle)
    anim = animation.FuncAnimation(
        fig, update_radius, fargs = (circle,), frames=30, interval=50)
    plt.title('Simple Circle Animation')
    plt.show()

g = 9.8

def get_intervals(u, theta):
    t_flight = float(2.0*u*math.sin(theta)/g)
    intervals = []
    start = 0.0
    interval = 0.005
    while start < t_flight:
        intervals.append(start)
        start = start + interval
    return intervals

def update_position(i, circle, intervals, u, theta):
    t = intervals[i]
    x = float(u*math.cos(theta)*t)
    y = float(u*math.sin(theta)*t - 0.5*g*t*t)
    circle.center = x, y
    return circle,

def create_animation_traj(u, theta):
    intervals = get_intervals(u, theta)
    xmin = 0.0
    xmax = float(u*math.cos(theta)*intervals[-1])
    ymin = 0.0
    t_max = float(u*math.sin(theta)/g)
    ymax = float(u*math.sin(theta)*t_max - 0.5*g*t_max**2.0)
    fig = plt.gcf()
    ax = plt.axes(xlim=(xmin, xmax), ylim=(ymin, ymax))
    circle = plt.Circle((xmin, ymin), 1.0)
    ax.add_patch(circle)
    anim = animation.FuncAnimation(fig, update_position,
        fargs=(circle, intervals, u, theta),
        frames=len(intervals),
        interval=1, repeat = False)
    plt.title('Projectile Motion')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

def draw_square():
    square = plt.Polygon([(1,1), (5,1), (5,5), (1,5)], closed=True, fc='b')
    return square


def draw_circle(x, y):
    circle = plt.Circle((x, y), 0.5, fc='w')
    return circle

def circle_in_square():
    ax = plt.axes(xlim=(0,6), ylim=(0,6))
    square = draw_square()
    ax.add_patch(square)
    y = 1.5
    while y < 5:
        x = 1.5
        while x < 5:
            c = draw_circle(x,y)
            ax.add_patch(c)
            x += 1.0
        y+= 1.0
    ax.set_aspect('equal')
    plt.show()

def trans_1(p):
    x = 0.5*float(p[0])
    y = 0.5*float(p[1])
    return x, y


def trans_2(p):
    x = 0.5*float(p[0]) + 0.5
    y = 0.5*float(p[1]) + 0.5
    return x, y

def trans_3(p):
    x = 0.5*float(p[0]) + 1.0
    y = 0.5*float(p[1])
    return x, y

def transf(p):
    tran = [trans_1, trans_2, trans_3]
    t = random.choice(tran)
    x, y = t(p)
    return x, y

def frac(p, n):
    x = [p[0]]
    y = [p[1]]
    for i in range(n):
        p = transf(p)
        x.append(p[0])
        y.append(p[1])
    return x, y

def frac_full():
    p = (0.0, 0.0)
    try:
        n = int(raw_input('Enter the number of iterations: '))
    except ValueError:
        print('oops')
    else:
        x, y = frac(p, n)
        plt.plot(x, y, 'o')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()

def hen_tran(p):
    x = float(p[1] + 1.0 - (1.4*(p[0]**2.0)))
    y = float(0.3*p[0])
    return x, y

def hen_frac(p, n):
    x = [p[0]]
    y = [p[1]]
    for i in range(n):
        p = hen_tran(p)
        x.append(p[0])
        y.append(p[1])
    return x, y

def hen():
    p = (1.0, 1.0)
    n = 20000
    x, y = hen_frac(p, n)
    print(max(x), min(x), max(y), min(y))
    ax = plt.axes(xlim=(min(x), max(x)), ylim=(min(y), max(y)))
    plt.plot(x, y, 'o')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
