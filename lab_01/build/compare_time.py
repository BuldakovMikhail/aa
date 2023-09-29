from time import process_time_ns
import matplotlib.pyplot as plt

from algorithms import *


def generate_strings(string_length=5):
    s1 = ""
    s2 = ""

    for _ in range(string_length):
        s1 += "a"
        s2 += "b"

    return s1, s2


def time_analysis(function, iterations, length):
    string_1, string_2 = generate_strings(length)

    time_start = process_time_ns()

    for _ in range(iterations):
        function(string_1, string_2)

    time_stop = process_time_ns()

    return (time_stop - time_start) / iterations


def print_measurement_res(
    sizes,
    time_lev_table,
    time_dam_lev_table,
    time_dam_lev_recursion,
    time_dam_lev_recursion_cash,
):
    print("-" * 136)

    print(
        "|{:^10s}|{:^30s}|{:^30s}|{:^30s}|{:^30s}|".format(
            "Длина",
            "Левенштейн (и)",
            "Дамерау-Левенштейн (и)",
            "Дамерау-Левенштейн (р)",
            "Дамерау-Левенштейн (рк)",
        )
    )

    print("-" * 136)

    with open("dist.csv", "w") as dist:
        for i in range(len(sizes)):
            print(
                "|{:^10d}|{:^30.2e}|{:^30.2e}|{:^30.2e}|{:^30.2e}|".format(
                    sizes[i],
                    time_lev_table[i],
                    time_dam_lev_table[i],
                    time_dam_lev_recursion[i],
                    time_dam_lev_recursion_cash[i],
                )
            )

            temp = [
                str(sizes[i]),
                str(time_lev_table[i]),
                str(time_dam_lev_table[i]),
                str(time_dam_lev_recursion[i]),
                str(time_dam_lev_recursion_cash[i]),
            ]

            dist.write(" & ".join(temp) + "//" + "\n" + "\hline" + "\n")

    print("-" * 136)


def build_graph(
    sizes,
    time_lev_table,
    time_dam_lev_table,
    time_dam_lev_recursion,
    time_dam_lev_recursion_cash,
):
    fig1 = plt.figure(figsize=(10, 7))
    plot = fig1.add_subplot()
    plot.plot(sizes, time_lev_table, label="Левенштейн (матричная)", marker=">")
    plot.plot(
        sizes, time_dam_lev_table, label="Дамерау-Левенштейн (матричная)", marker="+"
    )
    plot.plot(
        sizes,
        time_dam_lev_recursion,
        label="Дамерау-Левенштейн (рекурсивная)",
        marker="v",
    )
    plot.plot(
        sizes,
        time_dam_lev_recursion_cash,
        label="Дамерау-Левенштейн (рекурсивная с кешем)",
        marker="D",
    )

    plt.legend()
    plt.grid()
    plt.title("Сравнение алгоритмом по времени")
    plt.ylabel("Затраченное время (с)")
    plt.xlabel("Длина (кол-во букв)")
    plt.yscale("log")

    plt.show()


def compare_time():
    time_lev_table = []
    time_dam_lev_table = []
    time_dam_lev_recursion_cash = []
    time_dam_lev_recursion = []

    sizes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for n in sizes:
        time_lev_table.append(time_analysis(levenstein, 2000, n))
        time_dam_lev_table.append(time_analysis(damerau_levenstein_iter, 2000, n))
        time_dam_lev_recursion_cash.append(
            time_analysis(damerau_levenstein_rec_cash, 200, n)
        )
        time_dam_lev_recursion.append(time_analysis(damerau_levenstein_rec, 200, n))

    print_measurement_res(
        sizes,
        time_lev_table,
        time_dam_lev_table,
        time_dam_lev_recursion,
        time_dam_lev_recursion_cash,
    )

    build_graph(
        sizes,
        time_lev_table,
        time_dam_lev_table,
        time_dam_lev_recursion,
        time_dam_lev_recursion_cash,
    )
