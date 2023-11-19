import numpy as np
import random
import time

def generate_matrix(matrix_type, size=10):
    matrix = [[0] * size for _ in range(size)]

    for i in range(size):
        for j in range(size):
            if matrix_type == "graph":
                matrix[i][j] = random.randint(0, 1)
            elif matrix_type == "default_value":
                matrix[i][j] = 0.0

    if matrix_type == "graph":
        for i in range(size):
            matrix[i][i] = 0

    return matrix

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(f"{element:<4}", end=" ")
        print()

def main():
    random.seed(time.time())  # Для відтворюваності результатів

    digraph = generate_matrix("graph")
    transition = generate_matrix("default_value")

    print("Graph:")
    print_matrix(digraph)

    # Обчислюємо елементи відповідної перехідної матриці
    for i in range(len(digraph)):
        row_sum = sum(digraph[i])
        if row_sum > 0:
            transition[i] = [float(digraph[i][j]) / row_sum for j in range(len(digraph[i]))]
        else:
            transition[i] = [1.0 / len(digraph) for _ in range(len(digraph[i]))]

    # Виводимо вказану перехідну матрицю
    print("Here is the corresponding Transition Matrix:")
    print_matrix(transition)

    # Перераховуємо елементи перехідної матриці
    alpha = 0.85
    for i in range(len(transition)):
        for j in range(len(transition[i])):
            entry = transition[i][j]
            entry = alpha * entry + (1.0 - alpha) / len(digraph)
            transition[i][j] = entry

    # Виводимо модифіковану перехідну матрицю
    print("Here is the adjusted Transition Matrix:")
    print_matrix(transition)

    # Ініціалізуємо поточну матрицю ступенів
    current = [[1.0 if i == j else 0.0 for j in range(len(digraph))] for i in range(len(digraph))]

    # Головний цикл для відображення послідовності матриць ступенів
    step = 0
    while True:
        # Обчислюємо наступну матрицю ступенів
        current = np.dot(current, transition)

        # Виводимо поточну матрицю ступенів
        print(f"The Transition Matrix to power {step + 1}:")
        print_matrix(current)

        # Перевіряємо, чи досягнуто стаціонарного вектора
        square_diff = sum((current[i][j] - current[0][j]) ** 2 for j in range(len(digraph)) for i in range(1, len(digraph)))
        if square_diff < 0.00001:
            break

        step += 1

    print()

    # Виводимо стаціонарний вектор з літерами імен вузлів
    rank = [current[0][j] for j in range(len(digraph))]
    node = list(range(len(digraph)))

    print("Here is the resulting stationary vector:")
    print(rank)
    print(node)

    # Сортуємо компоненти вектора за спаданням
    sorted_indices = sorted(range(len(rank)), key=lambda k: rank[k], reverse=True)
    rank = [rank[i] for i in sorted_indices]
    node = [node[i] for i in sorted_indices]

    # Виводимо відсортований вектор стаціонарності
    print("Here is the resulting Rank-Punk vector:")
    print(rank)
    print(node)

if __name__ == "__main__":
    main()
