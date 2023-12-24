import matplotlib.pyplot as plt


def twink_standard_search(s, substr):
    counter = 0

    for i in range(len(s) - len(substr) + 1):
        flag = 0
        for j in range(len(substr)):
            counter += 1
            if s[i + j] != substr[j]:
                flag = 1
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
        counter += 1
        if j < len(substr) and s[i] == substr[j]:
            j += 1
            if j == len(substr):
                return counter
        elif j > 0:
            j = next[j]
            i -= 1
        i += 1

    return counter


def place_in_position(len_str, substr, position):
    return "а" * position + substr + "а" * (len_str - position)


def generate_best(len_str, substr):
    return substr + "а" * (len_str - len(substr))


def generate_worst(len_str, substr):
    return "а" * (len_str - len(substr)) + substr


def generate_without_substr(len_str, substr):
    return "а" * len_str


def count_compares():
    sizes = [8, 9, 10, 11, 12, 13, 14, 15, 16]
    best_comp_kmp = []
    worst_comp_kmp = []
    without_comp_kmp = []

    best_comp_st = []
    worst_comp_st = []
    without_comp_st = []

    for s in sizes:
        st = generate_best(2**s, "аааааааааб")
        best_comp_kmp.append(twink_KMP(st, "аааааааааб"))
        best_comp_st.append(twink_standard_search(st, "аааааааааб"))

        st = generate_worst(2**s, "аааааааааб")
        worst_comp_kmp.append(twink_KMP(st, "аааааааааб"))
        worst_comp_st.append(twink_standard_search(st, "аааааааааб"))

        st = generate_without_substr(2**s, "аааааааааб")
        without_comp_kmp.append(twink_KMP(st, "аааааааааб"))
        without_comp_st.append(twink_standard_search(st, "аааааааааб"))

    true_sizes = [i for i in sizes]

    # fig1 = plt.figure(figsize=(12, 6))
    # ax1 = fig1.add_subplot()
    # ax1.set_title("Подстрока стоит в начале (алгоритм Кнута---Морриса---Пратта)")
    # ax1.bar(true_sizes, best_comp_kmp)

    fig2 = plt.figure(figsize=(12, 8))
    ax2 = fig2.add_subplot()
    ax2.set_title("Подстрока стоит в конце (алгоритм Кнута---Морриса---Пратта)")
    ax2.bar(true_sizes, worst_comp_kmp)

    fig3 = plt.figure(figsize=(12, 8))
    ax3 = fig3.add_subplot()
    ax3.set_title("Подстроки нет в строке (алгоритм Кнута---Морриса---Пратта)")
    ax3.bar(true_sizes, without_comp_kmp)

    # fig4 = plt.figure(figsize=(12, 6))
    # ax4 = fig4.add_subplot()
    # ax4.set_title("Подстрока стоит в начале (стандартный алгоритм)")
    # ax4.bar(true_sizes, best_comp_st)

    fig5 = plt.figure(figsize=(12, 6))
    ax5 = fig5.add_subplot()
    ax5.set_title("Подстрока стоит в конце (стандартный алгоритм)")
    ax5.bar(true_sizes, worst_comp_st)

    fig6 = plt.figure(figsize=(12, 6))
    ax6 = fig6.add_subplot()
    ax6.set_title("Подстроки нет в строке (стандартный алгоритм)")
    ax6.bar(true_sizes, without_comp_st)

    plt.show()


def count_compares_on_same_length():
    str_len = 256

    poss = list(range(0, 257, 8))
    substr = "аааааффффф"

    comp_kmp = []
    comp_st = []

    for p in poss:
        st = place_in_position(str_len, substr, p)
        comp_kmp.append(twink_KMP(st, substr))
        comp_st.append(twink_standard_search(st, substr))

    fig1 = plt.figure(figsize=(14, 8))
    ax1 = fig1.add_subplot()
    ax1.set_title("Количество сравнений для алгоритма Кнута---Морисса---Пратта")
    ax1.set_xlabel("Индекс подстроки")
    ax1.set_ylabel("Количество сравнений")
    ax1.bar(poss, comp_kmp, width=6, label="Алгоритм Кнута---Морриса---Пратта")
    ax1.legend()

    fig6 = plt.figure(figsize=(14, 8))
    ax6 = fig6.add_subplot()
    ax6.set_title("Количество сравнений для стандартного алгоритма")
    ax6.set_xlabel("Индекс подстроки")
    ax6.set_ylabel("Количество сравнений")
    ax6.bar(poss, comp_st, width=6, label="Стандартный алгоритм")
    ax6.legend()

    plt.show()


if __name__ == "__main__":
    # count_compares()
    count_compares_on_same_length()
