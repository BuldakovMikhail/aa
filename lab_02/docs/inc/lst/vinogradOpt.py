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
