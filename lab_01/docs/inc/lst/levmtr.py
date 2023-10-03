def m(a, b):
    return 0 if a == b else 1


def levenstein(s1, s2):
    matrix = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == 0 and j == 0:
                matrix[i][j] = 0
            elif i > 0 and j == 0:
                matrix[i][j] = i
            elif j > 0 and i == 0:
                matrix[i][j] = j
            else:
                matrix[i][j] = min(
                    [
                        matrix[i][j - 1] + 1,
                        matrix[i - 1][j] + 1,
                        matrix[i - 1][j - 1] + m(s1[i - 1], s2[j - 1]),
                    ]
                )
    return matrix[-1][-1]
