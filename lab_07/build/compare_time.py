from time import process_time
import matplotlib.pyplot as plt

import numpy as np

from algorithms import *


def generate_best(len_str, substr):
    return substr + "а" * (len_str - len(substr))


def generate_worst(len_str, substr):
    return "а" * (len_str - len(substr)) + substr


def generate_without_substr(len_str, substr):
    return "а" * len_str


def time_analysis_best(function, iterations, length):
    m_1 = generate_best(length, "аааааааааб")

    time_start = process_time()

    for _ in range(iterations):
        function(m_1, "аааааааааб")

    time_stop = process_time()

    return (time_stop - time_start) / iterations


def time_analysis_worst(function, iterations, length):
    m_1 = generate_worst(length, "аааааааааб")

    time_start = process_time()

    for _ in range(iterations):
        function(m_1, "аааааааааб")

    time_stop = process_time()

    return (time_stop - time_start) / iterations


def time_analysis_without(function, iterations, length):
    m_1 = generate_without_substr(length, "аааааааааб")

    time_start = process_time()

    for _ in range(iterations):
        function(m_1, "аааааааааб")

    time_stop = process_time()

    return (time_stop - time_start) / iterations


def print_measurement_res(sizes, time_kmp, time_st):
    print("-" * 136)

    print(
        "|{:^10s}|{:^30s}|{:^30s}|".format(
            "Размер", "Кнута---Морриса---Пратта", "Стандартный"
        )
    )

    print("-" * 74)

    with open("dist.csv", "w") as dist:
        for i in range(len(sizes)):
            print(
                "|{:^10d}|{:^30.2e}|{:^30.2e}|".format(
                    sizes[i], time_kmp[i], time_st[i]
                )
            )

            temp = [
                "{:d}".format(sizes[i]),
                "{:.3e}".format(time_kmp[i]),
                "{:.3e}".format(time_st[i]),
            ]

            dist.write(" $&$ ".join(temp) + r"$\\" + "\n" + "\hline" + "\n")

    print("-" * 136)


def build_graph(sizes, time_kmp, time_st):
    fig1 = plt.figure(figsize=(10, 7))
    plot = fig1.add_subplot()
    plot.plot(sizes, time_kmp, label="Алгоритм Кнута---Морриса--Пратта", marker=">")
    plot.plot(sizes, time_st, label="Стандартный алгоритм", marker="+")

    plt.legend()
    plt.grid()
    plt.title("Сравнение реализаций алгоритмов по времени выполнения")
    plt.ylabel("Затраченное время (с)")
    plt.xlabel("Размер строк")
    # plt.yscale("log")

    plt.show()


def compare_time():
    time_kmp = []
    time_st = []

    temp = [8, 9, 10, 11, 12, 13, 14, 15, 16]
    sizes = [2**i for i in temp]

    # for n in sizes:
    #     print("n= ", n)

    #     time_kmp.append(time_analysis_best(KMP, 500000, n))
    #     time_st.append(time_analysis_best(standard_search, 500000, n))

    # with open("kmp_best.log", "w") as dist:
    #     print(time_kmp, file=dist)

    # with open("standard_best.log", "w") as dist:
    #     print(time_st, file=dist)

    # print_measurement_res(sizes, time_kmp, time_st)

    # build_graph(sizes, time_kmp, time_st)

    # -----------------------------------------------------

    # time_kmp = []
    # time_st = []

    # for n in sizes:
    #     print("n= ", n)

    #     time_kmp.append(time_analysis_worst(KMP, 250, n))
    #     time_st.append(time_analysis_worst(standard_search, 250, n))

    # with open("kmp_worst.log", "w") as dist:
    #     print(time_kmp, file=dist)

    # with open("standard_worst.log", "w") as dist:
    #     print(time_st, file=dist)

    # print_measurement_res(sizes, time_kmp, time_st)

    # build_graph(sizes, time_kmp, time_st)

    # # -----------------------------------------------------

    time_kmp = []
    time_st = []

    for n in sizes:
        print("n= ", n)

        time_kmp.append(time_analysis_without(KMP, 250, n))
        time_st.append(time_analysis_without(standard_search, 250, n))

    with open("kmp_without.log", "w") as dist:
        print(time_kmp, file=dist)

    with open("standard_without.log", "w") as dist:
        print(time_st, file=dist)

    print_measurement_res(sizes, time_kmp, time_st)

    build_graph(sizes, time_kmp, time_st)


if __name__ == "__main__":
    compare_time()
