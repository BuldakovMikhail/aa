def damerau_levenstein_rec_cash(s1, s2):
    d = [[-1] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    def get_value(s1, s2):
        if d[len(s1)][len(s2)] == -1:
            d[len(s1)][len(s2)] = dlrc(s1, s2)

        return d[len(s1)][len(s2)]

    def dlrc(s1, s2):
        if len(s1) == 0 or len(s2) == 0:
            d[len(s1)][len(s2)] = max(len(s1), len(s2))
            return d[len(s1)][len(s2)]

        dlr1 = get_value(s1[:-1], s2) + 1
        dlr2 = get_value(s1, s2[:-1]) + 1
        dlr3 = get_value(s1[:-1], s2[:-1]) + m(s1[-1], s2[-1])

        temp = min([dlr1, dlr2, dlr3])

        if len(s1) > 1 and len(s2) > 1 and s1[-1] == s2[-2] and s1[-2] == s2[-1]:
            dlr4 = get_value(s1[:-2], s2[:-2]) + 1
            temp = min(temp, dlr4)

        d[len(s1)][len(s2)] = temp

        return temp

    return dlrc(s1, s2)
