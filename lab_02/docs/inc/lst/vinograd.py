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
