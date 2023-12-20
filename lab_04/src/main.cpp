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

int main() {
    setlocale(LC_ALL, "");
    int opt;
    std::vector<std::wstring> words;

    while (true) {
        show_menu();
        std::wcin >> opt;

        if (opt == 0)
            break;
        else if (opt == 1) {
            words = read_words_from_file("../data/data.txt");
            if (words.empty())
                std::cout << "Ничего не прочитали" << std::endl;

            print_arr(words, false);
        } else if (opt == 2) {
            std::wstring word;
            int max_errors;
            int k;

            bool is_capital = false;

            std::cout << "Введите слово: ";
            std::wcin >> word;

            if (std::isupper(word[0]))
                is_capital = true;
            std::transform(word.begin(), word.end(), word.begin(),
                           [](unsigned char c) { return std::tolower(c); });

            std::cout << "Максимальное число ошибок: ";
            std::wcin >> max_errors;

            std::cout << "Сколько слов вывести: ";
            std::wcin >> k;


            auto res = get_closest_words(words, word, k, max_errors);
            std::cout << "Результат: " << std::endl;
            print_arr(res, is_capital);

        } else if (opt == 3) {
            std::wstring word;
            int max_errors;
            int k;
            int num_threads;

            bool is_capital = false;

            std::cout << "Введите слово: ";
            std::wcin >> word;

            std::cout << "Максимальное число ошибок: ";
            std::wcin >> max_errors;

            std::cout << "Сколько слов вывести: ";
            std::wcin >> k;

            std::cout << "Количество потоков: ";
            std::wcin >> num_threads;

            auto res = get_closest_words_mt(words, word, k, max_errors, num_threads);
            std::cout << "Результат: " << std::endl;
            print_arr(res, is_capital);
        } else if (opt == 4) { ;
        } else { ;
            break;
        }


    }

    return 0;
}
