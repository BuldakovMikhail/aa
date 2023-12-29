from algorithms import *
from compare_time import *


def show_menu():
    print(
        """
Меню:

1 - Отсортировать по возрастанию введенный массив всеми алгоритмами
2 - Провести замерный эксперимент
3 - Вывести функциональные тесты
0 - Выйти

Выберите пункт меню: 
          """
    )


def input_arr():
    print("Вводит целые числа через пробел: ")
    str_arr = input()

    arr = list(map(int, str_arr.split()))

    return arr


def run_sort(arr):
    print("-" * 20)
    print("Исходный массив: ", arr)
    print("Результат сортировки алгоритмом Шелла: ", shell_sort(arr.copy()))

    print("-" * 20)
    print("Исходный массив: ", arr)
    print("Результат гномьей сортировки: ", gnome_sort(arr.copy()))

    print("-" * 20)
    print("Исходный массив: ", arr)
    print("Результат пирамидальной сортировки: ", heap_sort(arr.copy()))
    print("-" * 20)


def func_tests():
    run_sort([1, 2, 3, 4, 5])
    run_sort([5, 4, 3, 2, 1])
    run_sort([])
    run_sort([1])
    run_sort([4, 1, 2, 3])
    run_sort([2, 1])
    run_sort([31, 57, 24, -10, 59])


def main():
    while True:
        show_menu()
        menu = int(input())

        if menu == 0:
            break
        elif menu == 1:
            arr = input_arr()
            run_sort(arr)

        elif menu == 2:
            compare_time()

        elif menu == 3:
            func_tests()

        else:
            print("Введен неверный пункт меню")


if __name__ == "__main__":
    main()
