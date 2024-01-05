from algorithms import *


def parametrization():
    alpha_arr = [num / 10 for num in range(1, 10, 2)]
    k_eva_arr = [num / 10 for num in range(1, 10, 2)]
    days_arr = [5, 25, 50, 100]

    tries = 10

    m1 = [
        [0, 34, 84, 64, 37, 51, 7, 55, 28, 10],
        [34, 0, 89, 61, 26, 64, 31, 82, 19, 48],
        [11, 16, 0, 46, 2, 75, 48, 65, 45, 62],
        [12, 30, 46, 0, 71, 37, 27, 70, 44, 25],
        [68, 20, 31, 36, 0, 47, 44, 72, 29, 82],
        [90, 78, 11, 44, 91, 0, 62, 43, 73, 77],
        [90, 33, 80, 8, 98, 48, 0, 99, 36, 71],
        [18, 16, 28, 22, 99, 62, 80, 0, 31, 63],
        [51, 77, 45, 91, 45, 41, 77, 40, 0, 26],
        [55, 67, 24, 8, 57, 29, 82, 50, 78, 0],
    ]
    m2 = [
        [0, 73, 27, 98, 40, 71, 11, 31, 17, 14],
        [5, 0, 19, 99, 74, 29, 43, 54, 94, 58],
        [78, 66, 0, 17, 79, 98, 74, 64, 39, 45],
        [4, 83, 56, 0, 71, 28, 32, 50, 96, 11],
        [36, 62, 51, 35, 0, 51, 62, 43, 39, 94],
        [6, 3, 53, 23, 42, 0, 10, 9, 46, 10],
        [25, 82, 23, 50, 32, 65, 0, 72, 69, 65],
        [53, 93, 55, 62, 71, 42, 79, 0, 79, 78],
        [65, 55, 45, 17, 44, 82, 68, 32, 0, 48],
        [93, 70, 2, 53, 62, 27, 76, 25, 81, 0],
    ]

    m3 = [
        [0, 22, 97, 48, 76, 64, 32, 66, 63, 50],
        [34, 0, 69, 46, 13, 63, 71, 99, 48, 83],
        [74, 21, 0, 3, 64, 49, 78, 38, 61, 42],
        [86, 4, 40, 0, 57, 16, 74, 36, 99, 98],
        [92, 51, 98, 42, 0, 38, 19, 28, 19, 18],
        [29, 92, 47, 30, 99, 0, 33, 86, 51, 4],
        [11, 9, 94, 46, 31, 5, 0, 46, 55, 45],
        [52, 95, 13, 3, 19, 25, 77, 0, 75, 14],
        [64, 49, 25, 36, 4, 96, 46, 50, 0, 61],
        [17, 54, 68, 80, 81, 84, 93, 35, 94, 0],
    ]

    matrices = [m1, m2, m3]

    for i, mat in enumerate(matrices):
        ideal = brut(mat, 0)[0]
        with open(f"parametr{i}.txt", "w") as dist:
            for a in alpha_arr:
                for k in k_eva_arr:
                    for d in days_arr:
                        m = -1

                        for _ in range(tries):
                            ant = ants(mat, 0, a, 1 - a, k, d)[0]
                            if ant > m:
                                m = ant

                        print(f"{a=}, {k=}, {d=}")
                        temp = f"{a}, {k}, {d}, {m}, {m - ideal}"
                        dist.write(temp + "\n")


def print_csv_as_tex_table(name):
    with open("tex.txt", "w") as dist:
        dist.write(r"\hline" + "\n")
        dist.write(r"$\alpha$ & $ \rho $ & $t_{max}$ & Res & Err \\" + "\n")
        with open(name, "r") as src:
            while x := src.readline():
                x = x.strip()
                dist.write(r"\hline" + "\n")
                x = x.replace(",", "&") + r"\\"
                dist.write(x + "\n")
            dist.write(r"\hline" + "\n")


# a = [
#     [0, 73, 27, 98, 40, 71, 11, 31, 17, 14],
#     [5, 0, 19, 99, 74, 29, 43, 54, 94, 58],
#     [78, 66, 0, 17, 79, 98, 74, 64, 39, 45],
#     [4, 83, 56, 0, 71, 28, 32, 50, 96, 11],
#     [36, 62, 51, 35, 0, 51, 62, 43, 39, 94],
#     [6, 3, 53, 23, 42, 0, 10, 9, 46, 10],
#     [25, 82, 23, 50, 32, 65, 0, 72, 69, 65],
#     [53, 93, 55, 62, 71, 42, 79, 0, 79, 78],
#     [65, 55, 45, 17, 44, 82, 68, 32, 0, 48],
#     [93, 70, 2, 53, 62, 27, 76, 25, 81, 0],
# ]

# b = [
#     [0, 22, 97, 48, 76, 64, 32, 66, 63, 50],
#     [34, 0, 69, 46, 13, 63, 71, 99, 48, 83],
#     [74, 21, 0, 3, 64, 49, 78, 38, 61, 42],
#     [86, 4, 40, 0, 57, 16, 74, 36, 99, 98],
#     [92, 51, 98, 42, 0, 38, 19, 28, 19, 18],
#     [29, 92, 47, 30, 99, 0, 33, 86, 51, 4],
#     [11, 9, 94, 46, 31, 5, 0, 46, 55, 45],
#     [52, 95, 13, 3, 19, 25, 77, 0, 75, 14],
#     [64, 49, 25, 36, 4, 96, 46, 50, 0, 61],
#     [17, 54, 68, 80, 81, 84, 93, 35, 94, 0],
# ]

if __name__ == "__main__":
    parametrization()
    print_csv_as_tex_table("parametr1.txt")