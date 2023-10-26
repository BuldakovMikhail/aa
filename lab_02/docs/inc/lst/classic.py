import numpy as np


def classical_mult(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Matrix shapes doesnt match")

    c = np.zeros((len(A), len(B[0])))

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                c[i][j] += A[i][k] * B[k][j]

    return c
