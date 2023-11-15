import numpy as np

def partial_pivot(A, n):
    for i in range(n):
        pivot_row = i
        for j in range(i + 1, n):
            if abs(A[j][i]) > abs(A[pivot_row][i]):
                pivot_row = j
        if pivot_row != i:
            A[[i, pivot_row]] = A[[pivot_row, i]]
        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            A[j] -= factor * A[i]

def back_substitute(A, n):
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        sum_val = sum(A[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (A[i][n] - sum_val) / A[i][i]

    return x


def gauss(A, b):
    n = len(b)
    augmented_matrix = np.concatenate((A, b.reshape(n, 1)), axis=1)
    augmented_matrix = augmented_matrix.astype(float)
    partial_pivot(augmented_matrix, n)
    x = back_substitute(augmented_matrix, n)
    return x