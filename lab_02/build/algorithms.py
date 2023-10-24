def classical_mult(A, B):
    if len(A) != len(B[0]):
        raise ValueError("Matrix shapes doesnt match")

    c = [[0] * len(A) for _ in range(len(B[0]))]

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
    if len(A) != len(B[0]):
        raise ValueError("Matrix shapes doesnt match")

    c = [[0] * len(A) for _ in range(len(B[0]))]
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
    if len(A) != len(B[0]):
        raise ValueError("Matrix shapes doesnt match")

    c = [[0] * len(A) for _ in range(len(B[0]))]
    row_factor = get_row_factor_opt(A)
    col_factor = get_col_factor_opt(B)

    temp = range(len(B) // 2)

    for i in range(len(A)):
        for j in range(len(B[0])):
            buff = -row_factor[i] - col_factor[j]
            for k in temp:
                buff += (A[i][k << 1] + B[(k << 1) + 1][j]) * (
                    A[i][(k << 1) + 1] + B[(k << 1)][j]
                )
            c[i][j] = buff

    if len(B) % 2 == 1:
        for i in range(len(A)):
            for j in range(len(B[0])):
                c[i][j] += A[i][-1] * B[-1][j]
    return c
