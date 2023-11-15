import numpy as np

def is_strictly_diagonally_dominant(matrix):
    diagonal = np.abs(matrix.diagonal())
    sum_abs_row = np.sum(np.abs(matrix), axis=1) - diagonal

    return np.all(diagonal > sum_abs_row)

def norm(a):
    max_row_sum = -1
    for i in range(len(a)):
        row_sum = sum(abs(a[i][j]) for j in range(len(a[i])))
        max_row_sum = max(max_row_sum, row_sum)
    return max_row_sum


def jacobi(A, b, eps, x=None):
    if not is_strictly_diagonally_dominant(A):
        raise ValueError("Matrix is not diagonally dominant. Jacobi method may not converge.")

    if x is None:
        x = np.zeros(len(A[0]))
        
    D = np.diag(A)
    R = A - np.diagflat(D)

    while True:
        x_new = (b - np.dot(R, x)) / D
        if np.linalg.norm(x_new - x, ord=np.inf) < eps:
            break
        x = x_new.copy()

    return x