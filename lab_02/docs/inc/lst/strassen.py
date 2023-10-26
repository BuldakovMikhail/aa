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
