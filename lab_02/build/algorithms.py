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


def get_row_factor(A):
    row_factor = [0] * len(A)
    for i in range(len(A)):
        for k in range(len(A[0]) // 2):
            row_factor[i] = row_factor[i] + A[i][2 * k + 1] * A[i][2 * k]

    return row_factor


def get_col_factor(B):
    col_factor = [0] * len(B[0])
    for i in range(len(B[0])):
        for k in range(len(B) // 2):
            col_factor[i] = col_factor[i] + B[2 * k + 1][i] * B[2 * k][i]

    return col_factor


def vinograd(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Matrix shapes doesnt match")

    c = np.zeros((len(A), len(B[0])))
    row_factor = get_row_factor(A)
    col_factor = get_col_factor(B)

    for i in range(len(A)):
        for j in range(len(B[0])):
            c[i][j] = -row_factor[i] - col_factor[j]
            for k in range(len(B) // 2):
                c[i][j] = c[i][j] + (A[i][2 * k] + B[2 * k + 1][j]) * (
                    A[i][2 * k + 1] + B[2 * k][j]
                )

    if len(B) % 2 == 1:
        for i in range(len(A)):
            for j in range(len(B[0])):
                c[i][j] = c[i][j] + A[i][len(B) - 1] * B[len(B) - 1][j]
    return c


def get_row_factor_opt(A):
    row_factor = [0] * len(A)
    temp = len(A[0]) // 2
    for i in range(len(A)):
        for k in range(temp):
            row_factor[i] += A[i][(k << 1) + 1] * A[i][k << 1]

    return row_factor


def get_col_factor_opt(B):
    col_factor = [0] * len(B[0])
    temp = len(B) // 2
    for i in range(len(B[0])):
        for k in range(temp):
            col_factor[i] += B[(k << 1) + 1][i] * B[k << 1][i]

    return col_factor


def vinograd_opt(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Matrix shapes doesnt match")

    c = np.zeros((len(A), len(B[0])))
    row_factor = get_row_factor_opt(A)
    col_factor = get_col_factor_opt(B)

    temp = range(len(B) // 2)

    for i in range(len(A)):
        for j in range(len(B[0])):
            buff = -row_factor[i] - col_factor[j]
            for k in temp:
                ks = k << 1
                buff += (A[i][ks] + B[ks + 1][j]) * (A[i][ks + 1] + B[ks][j])
            c[i][j] = buff

    if len(B) % 2 == 1:
        for i in range(len(A)):
            for j in range(len(B[0])):
                c[i][j] += A[i][-1] * B[-1][j]
    return c


def pad_to_power_of_two(A, B):
    n1, m1 = A.shape
    n2, m2 = B.shape

    n = max(n1, n2)
    m = max(m1, m2)

    target_size = 2 ** int(np.ceil(np.log2(max(m, n))))

    temp_A = np.zeros((target_size, target_size))
    temp_B = np.zeros((target_size, target_size))

    temp_A[:n1, :m1] = A
    temp_B[:n2, :m2] = B

    return temp_A, temp_B


def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0


def strassen(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Matrix shapes doesnt match")

    temp_A, temp_B = A, B
    if A.shape != B.shape or not is_power_of_two(len(A)):
        temp_A, temp_B = pad_to_power_of_two(A, B)

    def MSR(A, B):
        if len(A) == 1:
            return A @ B

        N = len(A)

        A11 = A[: N // 2, : N // 2]
        A12 = A[: N // 2, N // 2 :]
        A21 = A[N // 2 :, : N // 2]
        A22 = A[N // 2 :, N // 2 :]

        B11 = B[: N // 2, : N // 2]
        B12 = B[: N // 2, N // 2 :]
        B21 = B[N // 2 :, : N // 2]
        B22 = B[N // 2 :, N // 2 :]

        M1 = MSR(A11 + A22, B11 + B22)
        M2 = MSR(A21 + A22, B11)
        M3 = MSR(A11, B12 - B22)
        M4 = MSR(A22, B21 - B11)
        M5 = MSR(A11 + A12, B22)
        M6 = MSR(A21 - A11, B11 + B12)
        M7 = MSR(A12 - A22, B21 + B22)

        C11 = M1 + M4 - M5 + M7
        C12 = M3 + M5
        C21 = M2 + M4
        C22 = M1 - M2 + M3 + M6

        C = np.zeros((N, N))
        C[: N // 2, : N // 2] = C11
        C[: N // 2, N // 2 :] = C12
        C[N // 2 :, : N // 2] = C21
        C[N // 2 :, N // 2 :] = C22

        return C

    return MSR(temp_A, temp_B)
