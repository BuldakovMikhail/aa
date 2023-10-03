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
