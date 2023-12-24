def twink_standard_search(s, substr):
    counter = 0

    for i in range(len(s) - len(substr) + 1):
        flag = 0
        for j in range(len(substr)):
            if s[i + j] != substr[j]:
                flag = 1
                counter += 1
                break

        if not flag:
            return counter

    return counter


def twink_KMP(s, substr):
    counter = 0

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
            counter += 1
            j += 1
            if j == len(substr):
                return counter
        elif j > 0:
            j = next[j]
            i -= 1
        i += 1

    return counter


def generate_best(len_str, len_substr):
    return "б" * len_substr + "а" * (len_str - len_substr), "б" * len_substr


def generate_worst(len_str, len_substr):
    return "а" * (len_str - len_substr) + "б" * len_substr, "б" * len_substr


def generate_without_substr(len_str, len_substr):
    return "а" * len_str, "б" * len_substr


def count_compares():
    sizes = 
