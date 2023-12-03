from algorithms import *


def parametrization():
    alpha_arr = [num / 10 for num in range(1, 10)]
    k_eva_arr = [num / 10 for num in range(1, 10)]
    days_arr = [5, 25, 50, 100]

    tries = 10

    # m1 = [
    #     [0, 34, 84, 64, 37, 51, 7, 55, 28, 10],
    #     [34, 0, 89, 61, 26, 64, 31, 82, 19, 48],
    #     [11, 16, 0, 46, 2, 75, 48, 65, 45, 62],
    #     [12, 30, 46, 0, 71, 37, 27, 70, 44, 25],
    #     [68, 20, 31, 36, 0, 47, 44, 72, 29, 82],
    #     [90, 78, 11, 44, 91, 0, 62, 43, 73, 77],
    #     [90, 33, 80, 8, 98, 48, 0, 99, 36, 71],
    #     [18, 16, 28, 22, 99, 62, 80, 0, 31, 63],
    #     [51, 77, 45, 91, 45, 41, 77, 40, 0, 26],
    #     [55, 67, 24, 8, 57, 29, 82, 50, 78, 0],
    # ]

    # ideal1 = brut(m1, 0)[0]

    # with open("m1.csv", "w") as dist:
    #     for a in alpha_arr:
    #         for k in k_eva_arr:
    #             for d in days_arr:
    #                 m = -1

    #                 for _ in range(tries):
    #                     ant = ants(m1, 0, a, 1 - a, k, d)[0]
    #                     if ant > m:
    #                         m = ant

    #                 print(f"{a=}, {k=}, {d=}")
    #                 temp = f"{a}, {k}, {d}, {m}, {ideal1 - m}"
    #                 dist.write(temp + "\n")

    m2 = [
        [0, 2807, 2494, 4820, 8257, 8688, 2784, 7073, 5246, 5816],
        [6688, 0, 3579, 5313, 8630, 1530, 6084, 6745, 7040, 9483],
        [3070, 1462, 0, 5040, 8379, 1145, 9036, 4213, 8686, 9060],
        [7869, 6450, 5517, 0, 2936, 3890, 8459, 1535, 264, 6446],
        [7588, 1538, 4715, 957, 0, 3324, 8420, 705, 780, 2114],
        [5313, 7012, 6748, 3221, 8283, 0, 738, 2073, 1966, 9134],
        [3297, 2578, 8005, 2220, 4799, 8012, 0, 5366, 6696, 1371],
        [2885, 6139, 3617, 5044, 4018, 1991, 5720, 0, 3252, 3749],
        [6359, 5162, 2316, 2605, 3085, 8213, 8597, 8510, 0, 9288],
        [4739, 7850, 3077, 222, 3818, 8252, 8204, 8576, 4921, 0],
    ]

    ideal2 = brut(m2, 0)[0]

    with open("m2.csv", "w") as dist:
        for a in alpha_arr:
            for k in k_eva_arr:
                for d in days_arr:
                    m = -1

                    for _ in range(tries):
                        ant = ants(m2, 0, a, 1 - a, k, d)[0]
                        if ant > m:
                            m = ant

                    print(f"{a=}, {k=}, {d=}")
                    temp = f"{a}, {k}, {d}, {m}, {ideal2 - m}"
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


if __name__ == "__main__":
    # parametrization()
    print_csv_as_tex_table("m2.csv")
