import math
from sympy import *

epsilon = 0.0001

def f(x):
    return x**4+4*x-2

def dichotomy(a,b):
    root = None
    q = 0
    while abs(f(b)-f(a)) > epsilon:
        mid = (a+b)/2
        q = q+1
        if f(mid) == 0 or abs(f(mid)) < epsilon:
            root = mid
            break
        elif f(a)*f(mid) < 0:
            b = mid
        else:
            a = mid
    if root is None:
        print('Root not found')
    else:
        print(f'Dichotomy method: x = {root}')
        print(q)

def func():
    x = symbols('x')
    return f(x)
def funcderiv(x):
    a=str(diff(x))
    return a
def newton(func,funcderiv,x,max):
    def f(x):
        return eval(func)
    def df(x):
        return eval(funcderiv)
    if df(x) == 0:
        print('Zero derivative. No solution found.')
        return None
    for i in range(1,max):

        if abs(f(x)) < epsilon:
            print(x,' Found solution after ',i,' iterations.')
            return x
        i = x - (f(x) / df(x))
        x = i
    print(f"root = {x} after {max}")

def relaxation(func,funcderiv,min,max,x0):
    def f(x):
        return eval(func)
    def df(x):
        return eval(funcderiv)
    fda = abs(df(min))
    fdb = abs(df(max))
    min1 = fdb if fda > fdb else fda
    max1 = fdb if fda < fdb else fda
    print(f"Min: {min1} Max: {max1}")
    l = 2/(min1+max1)
    v = l * df(x0)
    if -2 < v and v < 1:
        print('Checked')
    q = (max1 - min1) / (max1 + min1)
    prev = 100
    x = max
    while abs(prev-x) > epsilon:
        prev = x
        x = prev - l*f(prev)
    print (x)

print("------------ Dichotomy method ------------")
dichotomy(0,2)
print("\n------------ Newton method ------------")
newton(str(func()),funcderiv(func()),1,10)
print("\n------------ Relaxation method ------------")
relaxation(str(func()),funcderiv(func()),1,3,2)

