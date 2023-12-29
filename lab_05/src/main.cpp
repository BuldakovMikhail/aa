#include <iostream>
#include <locale>
#include <codecvt>

#include "conveyor.h"
#include "atomic_queue.h"
#include "utils.h"

#include "measure_time.h"

void show_menu() {
    std::cout <<
              "Меню:\n"
              "1 - Запустить конвейер\n"
              "2 - Замерить время\n"
              "3 - Вывести статистику\n"
              "0 - Выйти\n"
              << std::endl;
    std::cout << "Выберите пункт меню: ";
}

int main() {
    setlocale(LC_ALL, "");

    int opt;
    std::vector<std::wstring> words = read_words_from_file("../russian_words.txt");
    std::wstring_convert<std::codecvt_utf8_utf16<wchar_t>> converter;

    while (true) {
        AtomicQueue<Request> start;
        AtomicQueue<Request> end;

        show_menu();
        std::cin >> opt;

        if (opt == 0)
            break;
        else if (opt == 1) {
            int size = 0;
            std::cout << "Введит количество заявок: ";
            std::cin >> size;

            generator(start, size, words);
            run_pipeline(start, end, "../russian_words.txt", "../res.log");
            int len = end.size();

            for (int i = 0; i < len; ++i) {
                auto req = end.front();
                end.pop();
                std::string narrow = converter.to_bytes(req.word);
                std::cout << narrow << '\t';

                for (const auto &w: req.res) {
                    auto temp = w;
                    std::string narrow = converter.to_bytes(temp);
                    std::cout << narrow << '\t';
                }
                std::cout << std::endl;
            }

        } else if (opt == 2) {
            getTimeResults(10, 80, 10, words);

        } else if (opt == 3) {
            int size = 0;
            std::cout << "Введит количество заявок: ";
            std::cin >> size;

            generator(start, size, words);
            run_pipeline(start, end, "../russian_words.txt", "../res.log");
            createReport(end);
        } else { ;
            break;
        }
    }

    return 0;
}
