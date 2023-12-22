#include <iostream>
#include "utils.h"
#include <algorithm>
#include <codecvt>
#include <locale>

#include "correcter.h"

void show_menu() {
    std::cout <<
              "Меню:\n"
              "1 - Прочитать корпус\n"
              "2 - Проверить слово (без потоков)\n"
              "3 - Проверить слово (с потоками)\n"
              "4 - Вывести статистику корпуса\n"
              "0 - Выйти\n"
              << std::endl;
    std::cout << "Выберите пункт меню: ";
}

int main() {
    setlocale(LC_ALL, "");
    int opt;
    std::vector<std::wstring> words;
    std::map<wchar_t, std::vector<std::wstring>> dict;
    std::wstring_convert<std::codecvt_utf8_utf16<wchar_t>> converter;

    while (true) {
        show_menu();
        std::cin >> opt;

        if (opt == 0)
            break;
        else if (opt == 1) {
            words = read_words_from_file("../russian_words.txt");
            if (words.empty())
                std::cout << "Ничего не прочитали" << std::endl;
            else
                std::cout << "Корпус считан" << std::endl;

            dict = get_segmented(words);
            /*print_arr(words, false);*/
        } else if (opt == 2) {
            std::string word;
            int max_errors;
            int k;

            bool is_capital = false;

            std::cout << "Введите слово: ";
            std::cin >> word;

            std::wstring wide = converter.from_bytes(word);

            if (std::isupper(wide[0]))
                is_capital = true;

            std::cout << "Максимальное число ошибок: ";
            std::cin >> max_errors;

            std::cout << "Сколько слов вывести: ";
            std::cin >> k;


            auto res = get_closest_words_with_segmented(dict, wide, k, max_errors);
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

            std::wstring wide = converter.from_bytes(word);

            std::cout << "Максимальное число ошибок: ";
            std::cin >> max_errors;

            std::cout << "Сколько слов вывести: ";
            std::cin >> k;

            std::cout << "Количество потоков: ";
            std::cin >> num_threads;

            auto res = get_closest_words_with_segmented_mt(dict, wide, k, max_errors, num_threads);
            if (res.empty()) {
                std::cout << "Слова не найдены " << std::endl;
            } else {
                std::cout << "Результат: " << std::endl;
                print_arr(res, is_capital);
            }
        } else if (opt == 4) {
            print_stats(dict);
        } else { ;
            break;
        }
    }

    return 0;
}
