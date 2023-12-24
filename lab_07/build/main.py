from algorithms import *
from count_compares import count_compares


def run_test(s, substr):
    print("-" * 30)
    print(f"Поиск подстроки {substr} в строке {s}")
    print(f"Результат стандартного алгоритма: {standard_search(s, substr)}")
    print(f"Результат алгоритма КМП: {KMP(s, substr)}")
    print("-" * 30)


def show_menu():
    print(
        """
    Меню:
    
    1 - Найти подстроку в строке (стандартный алгоритм)
    2 - Найти подстроку в строке (алгоритм КМП)
    3 - Функциональные тесты
    4 - Замеры количества сравнений
    0 - Выход
          """
    )


def func_tests():
    run_test("мама", "ам")
    run_test("абоба", "оба")
    run_test("абабабцб", "абабцб")
    run_test("мама", "пап")
    run_test("абабаба", "аб")
    run_test("мамы", "ы")
    run_test("ы", "ы")
    run_test("", "ы")
    run_test("ы", "")
    run_test("", "")
    run_test("абоба", "абобаабоба")


def main():
    while True:
        show_menu()
        m = int(input("Выберите пункт меню: "))
        if m == 0:
            break
        elif m == 1:
            s = input("Введит строку: ")
            substr = input("Введит подстроку: ")
            print(f"Результат (стандартный алгоритм): {standard_search(s, substr)}")
        elif m == 2:
            s = input("Введит строку: ")
            substr = input("Введит подстроку: ")
            print(f"Результат (алгоритм КМП): {KMP(s, substr)}")
        elif m == 3:
            func_tests()
        elif m == 4:
            count_compares()


if __name__ == "__main__":
    main()
