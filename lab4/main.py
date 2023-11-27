import numpy as np

def calculate_system_n(x):
    n = len(x)
    res = np.full(n, np.sum(x**2) - n)
    for i in range(n):
        res[i] -= x[i]**2 - x[i]**3
    return res

def calculate_jacobian_matrix_n(x):
    n = len(x)
    res = np.tile(2 * x, (n, 1))
    for i in range(n):
        res[i][i] *= 1.5 * x[i]

    return res

def newton(system, jacobian_matrix, x, epsilon):
    i = 0
    while True:
        i += 1
        z = np.linalg.solve(jacobian_matrix(x), system(x))
        x -= z
        if np.linalg.norm(z) < epsilon:
            return x

def relaxation(system, jacobian_matrix, x, epsilon):
    iter = 10000
    for i in range(iter):
        tau = 2 / np.linalg.norm(jacobian_matrix(x), ord=np.inf) - epsilon
        x1 = x - tau * system(x)
        if (x1 - x < epsilon):
            return x1, i
        x = x1
    return x

# Example usage:
epsilon = 0.0001

n = 10
x = np.full(n, 0.5)
result_newton_n = newton(calculate_system_n, calculate_jacobian_matrix_n, x, epsilon)
print("\nNewton method for n-dimensional system:")
print("Result:", result_newton_n)

x = np.full(n, 0.5)
result_relaxation_n = relaxation(calculate_system_n, calculate_jacobian_matrix_n, x, epsilon)
print("\nRelaxation method for n-dimensional system:")
print("Result:", result_relaxation_n)
