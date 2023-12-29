from time import process_time
import matplotlib.pyplot as plt

import numpy as np

from algorithms import *


from utils import generate_graph


def time_analysis(function, iterations, length):
    m_1 = generate_graph(length)

    time_start = process_time()

    for _ in range(iterations):
        function(m_1, 0)

    time_stop = process_time()

    return (time_stop - time_start) / iterations


def measure_time_ants(matrix, iterations):
    time_start = process_time()

    for i in range(iterations):
        ants(matrix, 0.5, 0.5, 0.5, 10, 0)

    time_stop = process_time()

    return (time_stop - time_start) / iterations


def print_measurement_res(
    sizes,
    time_brut,
    time_ants,
):
    print("-" * 136)

    print(
        "|{:^10s}|{:^30s}|{:^30s}|".format(
            "Количество городов", "Полный перебор", "Муравьиный алгоритм"
        )
    )

    print("-" * 136)

    with open("dist.csv", "w") as dist:
        for i in range(len(sizes)):
            print(
                "|{:^10d}|{:^30.2e}|{:^30.2e}|".format(
                    sizes[i], time_brut[i], time_ants[i]
                )
            )

            temp = [
                "{:d}".format(sizes[i]),
                "{:.3e}".format(time_brut[i]),
                "{:.3e}".format(time_ants[i]),
            ]

            dist.write(" $&$ ".join(temp) + r"$\\" + "\n" + "\hline" + "\n")

    print("-" * 136)


def build_graph(sizes, time_brut, time_ants):
    fig1 = plt.figure(figsize=(10, 7))
    plot = fig1.add_subplot()
    plot.plot(sizes, time_brut, label="Полный перебор", marker=">")
    plot.plot(sizes, time_ants, label="Муравьиный алгоритм", marker="+")

    plt.legend()
    plt.grid()
    plt.title("Сравнение реализаций алгоритмов по времени выполнения")
    plt.ylabel("Затраченное время (с)")
    plt.xlabel("Количество городов")
    # plt.yscale("log")

    plt.show()


def compare_time():
    time_brut = []
    time_ants = []

    sizes = list(range(4, 10))

    for n in sizes:
        print("n= ", n)

        time_brut.append(time_analysis(brut, 1000, n))
        time_ants.append(time_analysis(ants, 1000, n))

    with open("brut.log", "w") as dist:
        print(time_brut, file=dist)

    with open("ants.log", "w") as dist:
        print(time_ants, file=dist)

    print_measurement_res(sizes, time_brut, time_ants)

    build_graph(sizes, time_brut, time_ants)
