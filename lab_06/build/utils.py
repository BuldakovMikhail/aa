import numpy as np


def read_matrix_from_file(fname):
    matrix = []
    with open(fname, "r") as src:
        while line := src.readline():
            line = line.split()
            matrix.append(list(map(int, line)))

    return matrix


def matrix_input():
    n = int(input("Введит количество городов: "))

    matrix = []
    print("Вводите матрицу")

    for _ in range(n):
        temp = map(int, input().split())
        matrix.append(list(temp))

    return matrix


def generate_graph(size):
    a = np.random.randint(1, 100, size=(size, size))
    # b = np.random.randint(0, 2, size=(size, size))
    c = 1 - np.eye(size)

    return a * c


def print_matrix(matrix):
    print(*matrix, sep="\n")


def print_matrix_for_tex(matrix):
    for i in matrix:
        temp = ""
        for j in i:
            temp += f"{int(j)} & "
        temp = temp[:-2] + "\\\\"
        print(temp)


def print_matrix_for_copy(matrix):
    for i in matrix:
        temp = ""
        for j in i:
            temp += f"{int(j)}, "
        temp = temp[:-2]
        temp = "[" + temp + "],"
        print(temp)


if __name__ == "__main__":
    m = generate_graph(10)
    print_matrix_for_tex(m)
    print("-" * 10)
    print_matrix_for_copy(m)
