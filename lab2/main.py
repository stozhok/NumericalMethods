import numpy as np
from scipy.linalg import solve

import jacobi
import gauss
import generator as gen
import seidel

eps = 0.0001

A = gen.random_diagonally_dominant_matrix(3)
#b = np.array([15, 22, 3])
b = np.random.rand(3)
print("Gauss method Solution for the system:")
result1 = gauss.gauss(A, b)
print(result1)
print("----------")
print("Jacobi method Solution for the system:")
result2 = jacobi.jacobi(A, b,eps)
print(result2)
print("----------")
print("Seidel method Solution for the system:")
result3 = seidel.seidel(A, b, eps)
print(result3)
print("----------")
print("Solution for the system:")
print(solve(A,b))
