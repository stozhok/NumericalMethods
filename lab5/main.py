import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial import Polynomial as P
from scipy.interpolate import lagrange as lagrange_interp

def f(x):
    return 3*x - np.cos(x) - 1

def plot(x, y):
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    plt.plot(x, y)
    plt.show()

x = np.linspace(-6, 6, 100)
y = f(x)
plot(x, y)
a = -3
b = 7


xk = np.arange(a, b)
fxk = np.array(f(xk))

def numerator(i, c=0):
    if c >= xk.size:
        return 1
    n = numerator(i, c + 1)
    if c == i:
        return n
    return P([-xk[c], 1]) * n

def denominator(i, c=0):
    if c >= xk.size:
        return 1
    if c == i:
        return denominator(i, c + 1)
    return (xk[i] - xk[c]) * denominator(i, c + 1)

def partialPolynomial(i):
    return numerator(i) / denominator(i)

def lagrange():
    polynomial = fxk[0] * partialPolynomial(0)
    for i in range(1, xk.size):
        polynomial += fxk[i] * partialPolynomial(i)

    roots = polynomial.roots()
    maxRoot = np.max(np.real(roots))
    return maxRoot, polynomial

root, polynomial = lagrange()
print("lagrange:")
print(root)
print("Polynomial Coefficients:", polynomial.coef)

[x, y] = polynomial.linspace(100, [-6, 6])
plot(x, y)

def polynomials():
    arr = [P([-xk[0], 1])]
    for i in range(1, xk.size - 1):
        arr.append(arr[i - 1] * P([-xk[i], 1]))
    return arr

def newton():
    table = [fxk]
    for i in np.arange(1, xk.size):
        arr = np.zeros(xk.size - i)
        parr = table[i - 1]
        for j in range(0, parr.size - 1):
            arr[j] = (parr[j + 1] - parr[j]) / (xk[i + j] - xk[j])
        table.append(arr)

    arr = polynomials()
    polynomial = P([fxk[0]])
    for i in range(0, len(arr)):
        polynomial += table[i + 1][0] * arr[i]

    roots = polynomial.roots()
    maxRoot = np.max(np.real(roots))
    return maxRoot, polynomial

root, polynomial = newton()
print("newton:")
print(root)
print("Polynomial Coefficients:", polynomial.coef)

[x, y] = polynomial.linspace(100, [-6, 6])
plot(x, y)



