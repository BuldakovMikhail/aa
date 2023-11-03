from time import process_time
import matplotlib.pyplot as plt

import numpy as np

from algorithms import *


def generate_arr(n=5):
    arr = list(range(n, -1, -1))
    return arr


def generate_arr_rand(n=5):
    arr = np.random.randint(0, n, size=n)
    return arr


def generate_arr_sorted(n=5):
    arr = list(range(n))
    return arr


def time_analysis(function, iterations, length):
    m_1 = generate_arr(length)

    time_start = process_time()

    for _ in range(iterations):
        function(m_1)

    time_stop = process_time()

    return (time_stop - time_start) / iterations


def print_measurement_res(
    sizes,
    time_shell,
    time_gnome,
    time_heap,
):
    print("-" * 136)

    print(
        "|{:^10s}|{:^30s}|{:^30s}|{:^30s}|".format(
            "Размер",
            "Шелл",
            "Гномья",
            "Пирамидальная",
        )
    )

    print("-" * 136)

    with open("dist.csv", "w") as dist:
        for i in range(len(sizes)):
            print(
                "|{:^10d}|{:^30.2e}|{:^30.2e}|{:^30.2e}|".format(
                    sizes[i],
                    time_shell[i],
                    time_gnome[i],
                    time_heap[i],
                )
            )

            temp = [
                str(sizes[i]),
                str(time_shell[i]),
                str(time_gnome[i]),
                str(time_heap[i]),
            ]

            dist.write(" & ".join(temp) + "\\" + "\n" + "\hline" + "\n")

    print("-" * 136)


def build_graph(
    sizes,
    time_shell,
    time_gnome,
    time_heap,
):
    fig1 = plt.figure(figsize=(10, 7))
    plot = fig1.add_subplot()
    plot.plot(sizes, time_shell, label="Сортировка Шелла", marker=">")
    plot.plot(sizes, time_gnome, label="Гномья сортирова", marker="+")
    plot.plot(
        sizes,
        time_heap,
        label="Пирамидальная сортировка",
        marker="v",
    )

    plt.legend()
    plt.grid()
    plt.title("Сравнение реализаций алгоритмов по времени выполнения")
    plt.ylabel("Затраченное время (с)")
    plt.xlabel("Размер массивов")
    plt.yscale("log")

    plt.show()


def compare_time():
    time_shell = []
    time_gnome = []
    time_heap = []

    sizes = list(range(1000, 10000, 1000))

    for n in sizes:
        print("n= ", n)

        time_shell.append(time_analysis(shell_sort, 500, n))
        time_gnome.append(time_analysis(gnome_sort, 500, n))
        time_heap.append(time_analysis(heap_sort, 500, n))

    with open("shell.log", "w") as dist:
        print(time_shell, file=dist)

    with open("gnome.log", "w") as dist:
        print(time_gnome, file=dist)

    with open("heap.log", "w") as dist:
        print(time_heap, file=dist)

    print_measurement_res(
        sizes,
        time_shell,
        time_gnome,
        time_heap,
    )

    build_graph(
        sizes,
        time_shell,
        time_gnome,
        time_heap,
    )
