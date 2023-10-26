from algorithms import *


def main():
    a = np.array([[1, 2, 3], [4, 5, 6]])
    b = np.array([[1, 2], [3, 4], [5, 6]])

    print(a @ b)

    print(classical_mult(a, b))
    print(vinograd(a, b))
    print(vinograd_opt(a, b))
    print(strassen(a, b))


if __name__ == "__main__":
    main()
