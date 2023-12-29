def KMP(s, substr):
    next = [0] * (len(substr) + 1)

    for i in range(1, len(substr)):
        j = next[i]
        while j > 0 and substr[j] != substr[i]:
            j = next[j]
        if j > 0 or substr[j] == substr[i]:
            next[i + 1] = j + 1

    i, j = 0, 0
    while i < len(s):
        if j < len(substr) and s[i] == substr[j]:
            j += 1
            if j == len(substr):
                return i - j + 1
        elif j > 0:
            j = next[j]
            i -= 1
        i += 1

    return -1
