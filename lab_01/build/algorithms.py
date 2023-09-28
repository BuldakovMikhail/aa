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


def damerau_levenstein_iter(s1, s2):
    d = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    for i in range(len(d)):
        for j in range(len(d[0])):
            if i == 0 and j == 0:
                d[i][j] = 0
            elif i > 0 and j == 0:
                d[i][j] = i
            elif j > 0 and i == 0:
                d[i][j] = j
            elif i > 1 and j > 1 and s1[i - 1] == s2[j - 2] and s1[i - 2] == s2[j - 1]:
                d[i][j] = min(
                    [
                        d[i][j - 1] + 1,
                        d[i - 1][j] + 1,
                        d[i - 1][j - 1] + m(s1[i - 1], s2[j - 1]),
                        d[i - 2][j - 2] + 1,
                    ]
                )
            else:
                d[i][j] = min(
                    [
                        d[i][j - 1] + 1,
                        d[i - 1][j] + 1,
                        d[i - 1][j - 1] + m(s1[i - 1], s2[j - 1]),
                    ]
                )
    return d[-1][-1]


def damerau_levenstein_rec(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return max(len(s1), len(s2))
    temp = min(
        [
            damerau_levenstein_rec(s1[:-1], s2) + 1,
            damerau_levenstein_rec(s1, s2[:-1]) + 1,
            damerau_levenstein_rec(s1[:-1], s2[:-1]) + m(s1[-1], s2[-1]),
        ]
    )

    if len(s1) > 1 and len(s2) > 1 and s1[-1] == s2[-2] and s1[-2] == s2[-1]:
        temp = min(temp, damerau_levenstein_rec(s1[:-2], s2[:-2]) + 1)

    return temp


def damerau_levenstein_rec_cash(s1, s2):
    d = [[-1] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    def dlrc(s1, s2):
        if len(s1) == 0 or len(s2) == 0:
            d[len(s1)][len(s2)] = max(len(s1), len(s2))
            return d[len(s1)][len(s2)]

        if d[len(s1[:-1])][len(s2)] >= 0:
            dlr1 = d[len(s1[:-1])][len(s2)]
        else:
            # Случай если значение не в кеше, то вычисляем и "кешируем"
            dlr1 = dlrc(s1[:-1], s2)
            d[len(s1[:-1])][len(s2)] = dlr1

        if d[len(s1)][len(s2[:-1])] >= 0:
            dlr2 = d[len(s1)][len(s2[:-1])]
        else:
            # Случай если значение не в кеше, то вычисляем и "кешируем"
            dlr2 = dlrc(s1, s2[:-1])
            d[len(s1)][len(s2[:-1])] = dlr2

        if d[len(s1[:-1])][len(s2[:-1])] >= 0:
            dlr3 = d[len(s1[:-1])][len(s2[:-1])]
        else:
            # Случай если значение не в кеше, то вычисляем и "кешируем"
            dlr3 = dlrc(s1[:-1], s2[:-1])
            d[len(s1[:-1])][len(s2[:-1])] = dlr3

        temp = min([dlr1 + 1, dlr2 + 1, dlr3 + m(s1[-1], s2[-1])])

        if len(s1) > 1 and len(s2) > 1 and s1[-1] == s2[-2] and s1[-2] == s2[-1]:
            if d[len(s1[:-2])][len(s2[:-2])] >= 0:
                dlr4 = d[len(s1[:-2])][len(s2[:-2])]
            else:
                # Случай если значение не в кеше, то вычисляем и "кешируем"
                dlr4 = dlrc(s1[:-2], s2[:-2])
                d[len(s1[:-2])][len(s2[:-2])] = dlr4
            temp = min(temp, dlr4 + 1)

        d[len(s1)][len(s2)] = temp

        return temp

    return dlrc(s1, s2)
