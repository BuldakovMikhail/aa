from algorithms import *
from compare_time import *


def show_menu():
    print(
        """
Меню:

1 - Умножить две матрицы всеми способами
2 - Провести замерный эксперимент
3 - Вывести функциональные тесты
0 - Выйти

Выберите пункт меню: 
          """
    )


def input_matrices():
    n, m = list(map(int, input("Введите n, m матрицы A через пробел: ").split()))

    A = np.zeros((n, m))
    print("Введите матрицу: ")
    for i in range(n):
        row = list(map(float, input(f"Строка {i + 1}: ").split()))
        if len(row) != m:
            raise ValueError("Shape doesnt match")

        A[i] = row

    n, m = list(map(int, input("Введите n, m матрицы B через пробел: ").split()))

    B = np.zeros((n, m))
    print("Введите матрицу: ")
    for i in range(n):
        row = list(map(float, input(f"Строка {i + 1}: ").split()))
        if len(row) != m:
            raise ValueError("Shape doesnt match")

        B[i] = row

    return A, B


def test(A, B):
    print("-" * 60)
    print("Матрица A: ")
    print(A)
    print("Матрица B: ")
    print(B)
    print("Классический алгоритм AxB: ")
    print(classical_mult(A, B))

    print("Алгоритм Винограда AxB: ")
    print(vinograd(A, B))

    print("Алгоритм Винограда оптимизированный AxB: ")
    print(vinograd_opt(A, B))

    print("Алгоритм Штрассена AxB: ")
    print(strassen(A, B))

    print("-" * 60)


def func_tests():
    A = np.array([[1, 5, 7], [2, 6, 8], [3, 7, 9]])
    B = np.array([[]])

    try:
        test(A, B)
    except ValueError:
        print("Произошла ошибка")

    A = np.array([[1, 5, 7]])
    B = np.array([[1, 2, 3]])

    try:
        test(A, B)
    except ValueError:
        print("Произошла ошибка")

    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    B = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

    test(A, B)

    A = np.array([[3, 5], [2, 1], [9, 7]])
    B = np.array([[1, 2, 3], [4, 5, 6]])

    test(A, B)

    A = np.array([[10]])
    B = np.array([[35]])

    test(A, B)

    A = np.array([[1, 5, 7], [2, 6, 8], [3, 7, 9]])
    B = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    test(A, B)


def main():
    while True:
        show_menu()
        menu = int(input())

        if menu == 0:
            break
        elif menu == 1:
            A, B = None, None
            try:
                A, B = input_matrices()
            except ValueError:
                print("Ошибка ввода")
                continue

            if len(A[0]) != len(B):
                print("Матрицы нельзя умножить")
                continue

            print("Результат умножения по классическому алгоритму: ")
            print(classical_mult(A, B))

            print("Результат умножения по алгоритму Винограда: ")
            print(vinograd(A, B))

            print("Результат умножения по алгоритму Винограда с оптимизацией: ")
            print(vinograd_opt(A, B))

            print("Результат умножения по алгоритму Штрассена: ")
            print(strassen(A, B))

        elif menu == 2:
            compare_time()

        elif menu == 3:
            func_tests()
        else:
            print("Введен неверный пункт меню")


if __name__ == "__main__":
    main()
