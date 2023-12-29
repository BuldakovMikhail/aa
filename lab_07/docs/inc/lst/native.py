def standard_search(s, substr):
    for i in range(len(s) - len(substr) + 1):
        flag = 0
        for j in range(len(substr)):
            if s[i + j] != substr[j]:
                flag = 1
                break

        if not flag:
            return i

    return -1
