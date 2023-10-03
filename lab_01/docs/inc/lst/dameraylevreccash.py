def damerau_levenstein_rec_cash(s1, s2):
    d = [[-1] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    def dlrc(s1, s2):
        if len(s1) == 0 or len(s2) == 0:
            d[len(s1)][len(s2)] = max(len(s1), len(s2))
            return d[len(s1)][len(s2)]

        if d[len(s1[:-1])][len(s2)] >= 0:
            dlr1 = d[len(s1[:-1])][len(s2)]
        else:
            dlr1 = dlrc(s1[:-1], s2)
            d[len(s1[:-1])][len(s2)] = dlr1

        if d[len(s1)][len(s2[:-1])] >= 0:
            dlr2 = d[len(s1)][len(s2[:-1])]
        else:
            dlr2 = dlrc(s1, s2[:-1])
            d[len(s1)][len(s2[:-1])] = dlr2

        if d[len(s1[:-1])][len(s2[:-1])] >= 0:
            dlr3 = d[len(s1[:-1])][len(s2[:-1])]
        else:
            dlr3 = dlrc(s1[:-1], s2[:-1])
            d[len(s1[:-1])][len(s2[:-1])] = dlr3

        temp = min([dlr1 + 1, dlr2 + 1, dlr3 + m(s1[-1], s2[-1])])

        if len(s1) > 1 and len(s2) > 1 and s1[-1] == s2[-2] and s1[-2] == s2[-1]:
            if d[len(s1[:-2])][len(s2[:-2])] >= 0:
                dlr4 = d[len(s1[:-2])][len(s2[:-2])]
            else:
                dlr4 = dlrc(s1[:-2], s2[:-2])
                d[len(s1[:-2])][len(s2[:-2])] = dlr4
            temp = min(temp, dlr4 + 1)

        d[len(s1)][len(s2)] = temp

        return temp

    return dlrc(s1, s2)
