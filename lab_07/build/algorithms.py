def standard_search(s, substr):
    for i in range(len(s)):
        if s[i : i + len(substr)] == substr:
            return i
    return -1


def KMP(text, pattern):
    chars = list(pattern)
    next = [0] * (len(pattern) + 1)
    for i in range(1, len(pattern)):
        j = next[i]

        while j > 0 and chars[j] is not chars[i]:
            j = next[j]
        if j > 0 or chars[j] == chars[i]:
            next[i + 1] = j + 1
    i, j = 0, 0
    while i < len(text):
        if j < len(pattern) and text[i] == pattern[j]:
            j = j + 1
            if j == len(pattern):
                return i - j + 1
        elif j > 0:
            j = next[j]
            i = i - 1
        i = i + 1


print(standard_search("мама", "ам"))
print(KMP("мама", "ам"))


print(standard_search("aboba", "oba"))
print(KMP("aboba", "oba"))

print(standard_search("aaaaabbbacbacbacbab", "bab"))
print(KMP("aaaaabbbacbacbacbab", "bab"))
