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
