from algorithms import *


def main():
    a = [[1, 2, 3], [4, 5, 6]]
    b = [[1, 2], [3, 4], [5, 6]]

    print(classical_mult(a, b))
    print(vinograd(a, b))
    print(vinograd_opt(a, b))


if __name__ == "__main__":
    main()
