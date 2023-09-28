from algorithms import *

from compare_time import *


# \hline
# 		$\lambda$ & $\lambda$ & 0 & 0 & 0 & 0 \\
# 		\hline
# 		a & b & 1 & 1 & 1 & 1 \\
# 		\hline
# 		a & a & 0 & 0 & 0 & 0 \\
# 		\hline
# 		кот & скат & 2 & 2 & 2 & 2 \\
# 		\hline
# 		ab & ba & 2 & 1 & 1 & 1 \\
# 		\hline
# 		bba & abba & 1 & 1 & 1 & 1 \\
# 		\hline
# 		aboba & boba & 1 & 1 & 1 & 1 \\
# 		\hline
# 		abcdef & gh & 6 & 6 & 6 & 6 \\
# 		\hline


def test(s1, s2):
    print("----------------------------------------------------")
    print(f"Levenstein({s1}, {s2}): ", levenstein(s1, s2))
    print(f"Damerau-Levenstein_iter({s1}, {s2}): ", damerau_levenstein_iter(s1, s2))
    print(f"Damerau-Levenstein_rec({s1}, {s2}): ", damerau_levenstein_rec(s1, s2))
    print(
        f"Damerau-Levenstein_rec_cash({s1}, {s2}): ",
        damerau_levenstein_rec_cash(s1, s2),
    )
    print("----------------------------------------------------")


def show_menu():
    print(
        """
    
    1 - Расстояние Левенштейна (итеративно)
    2 - Расстояние Дамерау-Левенштейна (итеративно)
    3 - Расстояние Дамерау-Левенштейна (рекурсивно)
    4 - Расстояние Дамерау-Левенштейна (рекурсивно с кешированием)
    5 - Вывести результаты тестов
    6 - Замер времени
    0 - Выход

        """
    )


def main():
    show_menu()
    while x := int(input("Выберите опцию: ")):
        if x == 0:
            break
        elif x == 5:
            tests = [
                ("", ""),
                ("a", "b"),
                ("a", "a"),
                ("кот", "скат"),
                ("ab", "ba"),
                ("bba", "abba"),
                ("aboba", "boba"),
                ("abcdef", "gh"),
            ]

            for t in tests:
                test(*t)
            # test("ab", "ba")
            # test("vvvvvc", "bbbbbc")
        elif x == 1:
            s1 = input("Введите строку 1: ")
            s2 = input("Введите строку 2: ")
            print(f"Расстояние = {levenstein(s1, s2)}")
        elif x == 2:
            s1 = input("Введите строку 1: ")
            s2 = input("Введите строку 2: ")
            print(f"Расстояние = {damerau_levenstein_iter(s1, s2)}")
        elif x == 3:
            s1 = input("Введите строку 1: ")
            s2 = input("Введите строку 2: ")
            print(f"Расстояние = {damerau_levenstein_rec(s1, s2)}")
        elif x == 4:
            s1 = input("Введите строку 1: ")
            s2 = input("Введите строку 2: ")
            print(f"Расстояние = {damerau_levenstein_rec_cash(s1, s2)}")
        elif x == 6:
            compare_time()
        else:
            print("Неверная опция")

        show_menu()


if __name__ == "__main__":
    main()
