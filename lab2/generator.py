import numpy as np

def random_matrix(dim):
    return np.random.rand(dim,dim)

def random_int_matrix(dim,low=0,high=20):
    return np.random.randint(low,high,size=(dim,dim))

def random_diagonally_dominant_matrix(dim, low=0, high=20):
    A = np.random.randint(low, high, size=(dim, dim))
    np.fill_diagonal(A, np.sum(np.abs(A), axis=1) + 1)  # Зробимо матрицю строго діагонально-домінуючою
    return A

def hilbert_matrix(dim):
    h = np.zeros((dim, dim))
    for i in range(dim):
        for j in range(dim):
            h[i][j] = 1 / (i + j + 1)

    return h