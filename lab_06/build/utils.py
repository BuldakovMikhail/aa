import numpy as np


def read_matrix_from_file(fname):
    matrix = []
    with open(fname, "r") as src:
        while line := src.readline():
            line = line.split()
            matrix.append(list(map(int, line)))

    return matrix


def generate_graph(size):
    a = np.random.randint(1, 10, size=(size, size))
    # b = np.random.randint(0, 2, size=(size, size))
    c = 1 - np.eye(size)

    return a * c


def print_matrix(matrix):
    for i in matrix:
        temp = ""
        for j in i:
            temp += f"{int(j)}, "
        temp = temp[:-2]
        print(temp)


print_matrix(generate_graph(5))
