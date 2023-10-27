from time import process_time
import matplotlib.pyplot as plt

import numpy as np

from algorithms import *


def generate_matrix(n=5):
    s1 = np.random.rand(n, n)
    s2 = np.random.rand(n, n)
    return s1, s2


def time_analysis(function, iterations, length):
    m_1, m_2 = generate_matrix(length)

    time_start = process_time()

    for _ in range(iterations):
        function(m_1, m_2)

    time_stop = process_time()

    return (time_stop - time_start) / iterations


def print_measurement_res(
    sizes,
    time_classic,
    time_vinograd,
    time_vinograd_opt,
    time_strassen,
):
    print("-" * 136)

    print(
        "|{:^10s}|{:^30s}|{:^30s}|{:^30s}|{:^30s}|".format(
            "Порядок",
            "Классический",
            "Виноград",
            "Виноград оптим.",
            "Штрассен",
        )
    )

    print("-" * 136)

    with open("dist.csv", "w") as dist:
        for i in range(len(sizes)):
            print(
                "|{:^10d}|{:^30.2e}|{:^30.2e}|{:^30.2e}|{:^30.2e}|".format(
                    sizes[i],
                    time_classic[i],
                    time_vinograd[i],
                    time_vinograd_opt[i],
                    time_strassen[i],
                )
            )

            temp = [
                str(sizes[i]),
                str(time_classic[i]),
                str(time_vinograd[i]),
                str(time_vinograd_opt[i]),
                str(time_strassen[i]),
            ]

            dist.write(" & ".join(temp) + "\\" + "\n" + "\hline" + "\n")

    print("-" * 136)


def build_graph(
    sizes,
    time_classic,
    time_vinograd,
    time_vinograd_opt,
    time_strassen,
):
    fig1 = plt.figure(figsize=(10, 7))
    plot = fig1.add_subplot()
    plot.plot(sizes, time_classic, label="Классический алгоритм", marker=">")
    plot.plot(sizes, time_vinograd, label="Алгоритм Винограда", marker="+")
    plot.plot(
        sizes,
        time_vinograd_opt,
        label="Алгоритм Винограда с оптимизацией",
        marker="v",
    )
    # plot.plot(
    #     sizes,
    #     time_strassen,
    #     label="Алгоритм Штрассена",
    #     marker="D",
    # )

    plt.legend()
    plt.grid()
    plt.title("Сравнение реализаций алгоритмов по времени выполнения")
    plt.ylabel("Затраченное время (с)")
    plt.xlabel("Порядок матриц")
    plt.yscale("log")

    plt.show()


def compare_time():
    time_classic = []
    time_vinograd = []
    time_strassen = []
    time_vinograd_opt = []

    sizes = list(range(6, 53, 4))

    for n in sizes:
        print("n= ", n)

        time_classic.append(time_analysis(classical_mult, 500, n))
        time_vinograd.append(time_analysis(vinograd, 500, n))
        # time_strassen.append(time_analysis(strassen, 500, n))
        time_vinograd_opt.append(time_analysis(vinograd_opt, 500, n))

    with open("classic.log", "w") as dist:
        print(time_classic, file=dist)

    with open("vinograd.log", "w") as dist:
        print(time_vinograd, file=dist)

    with open("vinograd_opt.log", "w") as dist:
        print(time_vinograd_opt, file=dist)

    # with open("strassen.log", "w") as dist:
    #     print(time_strassen, file=dist)

    # print_measurement_res(
    #     sizes,
    #     time_classic,
    #     time_vinograd,
    #     time_vinograd_opt,
    #     time_strassen,
    # )

    build_graph(
        sizes,
        time_classic,
        time_vinograd,
        time_vinograd_opt,
        time_strassen,
    )
