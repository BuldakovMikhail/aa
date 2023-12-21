#include <iostream>
#include "levenstein.h"
#include "correcter.h"
#include "utils.h"
#include "measure_time.h"

#include <algorithm>

void show_menu() {
    std::cout <<
              "Меню:\n"
              "1 - Прочитать корпус\n"
              "2 - Проверить слово (без потоков)\n"
              "3 - Проверить слово (с потоками)\n"
              "4 - Функциональное тестирование\n"
              "5 - Замеры времени\n"
              "0 - Выйти\n"
              << std::endl;
    std::cout << "Выберите пункт меню: ";
}

void func_test(const std::vector<std::string> &words, const std::string &word, bool is_capital) {
    std::cout << "---------------------------" << std::endl;
    std::cout << "Слово: " << word << std::endl;
    std::cout << "Результат (без потоков): " << std::endl;
    auto res = get_closest_words(words, word, 3, 2);
    print_arr(res, is_capital);

    std::cout << "Результат (c потоками): " << std::endl;
    res = get_closest_words_mt(words, word, 3, 2, 2);
    print_arr(res, is_capital);
    std::cout << "---------------------------" << std::endl;
}

void run_tests() {
    std::vector<std::string> ftest_words = {"mama", "myla", "ramu"};
    func_test(ftest_words, "mama", true);
    func_test(ftest_words, "mamy", false);
    func_test(ftest_words, "myma", false);
    func_test(ftest_words, "ahtung", false);
    func_test({}, "ahtung", false);
    func_test({}, "", false);
    func_test(ftest_words, "", false);
}


int main() {
    setlocale(LC_ALL, "");
    int opt;
    std::vector<std::string> words;

    while (true) {
        show_menu();
        std::cin >> opt;

        if (opt == 0)
            break;
        else if (opt == 1) {
            words = read_words_from_file("../data/data.txt");
            if (words.empty())
                std::cout << "Ничего не прочитали" << std::endl;
            else
                std::cout << "Корпус считан" << std::endl;
            /*print_arr(words, false);*/
        } else if (opt == 2) {
            std::string word;
            int max_errors;
            int k;

            bool is_capital = false;

            std::cout << "Введите слово: ";
            std::cin >> word;

            if (std::isupper(word[0]))
                is_capital = true;
            std::transform(word.begin(), word.end(), word.begin(),
                           [](unsigned char c) { return std::tolower(c); });

            std::cout << "Максимальное число ошибок: ";
            std::cin >> max_errors;

            std::cout << "Сколько слов вывести: ";
            std::cin >> k;


            auto res = get_closest_words(words, word, k, max_errors);
            if (res.empty()) {
                std::cout << "Слова не найдены " << std::endl;
            } else {
                std::cout << "Результат: " << std::endl;
                print_arr(res, is_capital);
            }

        } else if (opt == 3) {
            std::string word;
            int max_errors;
            int k;
            int num_threads;

            bool is_capital = false;

            std::cout << "Введите слово: ";
            std::cin >> word;

            std::cout << "Максимальное число ошибок: ";
            std::cin >> max_errors;

            std::cout << "Сколько слов вывести: ";
            std::cin >> k;

            std::cout << "Количество потоков: ";
            std::cin >> num_threads;

            auto res = get_closest_words_mt(words, word, k, max_errors, num_threads);
            if (res.empty()) {
                std::cout << "Слова не найдены " << std::endl;
            } else {
                std::cout << "Результат: " << std::endl;
                print_arr(res, is_capital);
            }
        } else if (opt == 4) {
            run_tests();
        } else if (opt == 5) {
            /*measure_time_with_threads(1, 15, 1);*/
            measure_time_with_threads(1, 50, 2);

            measure_linear(1000, 11000, 1000);
        } else { ;
            break;
        }


    }

    return 0;
}
