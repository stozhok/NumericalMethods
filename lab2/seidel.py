import numpy as np


def is_strictly_diagonally_dominant(matrix):
    diagonal = np.abs(matrix.diagonal())
    sum_abs_row = np.sum(np.abs(matrix), axis=1) - diagonal

    return np.all(diagonal > sum_abs_row)

def norm(a):
    if a.ndim == 1:
        return np.max(np.abs(a))
    elif a.ndim == 2:
        return np.max(np.sum(np.abs(a), axis=1))
    else:
        raise ValueError("Input must be a 1D or 2D array.")

def seidel(A, b, eps, x = None):
    if not is_strictly_diagonally_dominant(A):
        raise ValueError("Matrix is not diagonally dominant. Jacobi method may not converge.")

    n = len(b)

    if x is None:
        x = np.zeros(len(A[0]))

    while True:
        x_old = x.copy()
        for i in range(n):
            sigma = sum(A[i][j] * x[j] for j in range(i))
            sigma += sum(A[i][j] * x_old[j] for j in range(i + 1, n))
            x[i] = (b[i] - sigma) / A[i, i]


        if norm(x - x_old) < eps:
            break

    return x
