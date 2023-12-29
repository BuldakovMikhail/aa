//
// Created by User on 20.12.2023.
//

#include <ctime>
#include <vector>
#include <string>
#include <iostream>
#include <fstream>

#include "measure_time.h"
#include "correcter.h"

std::vector<std::string> generate_array(size_t len, size_t word_size) {
    std::string temp(word_size, 'a');
    std::vector<std::string> res;

    for (int i = 0; i < len; ++i)
        res.push_back(temp);

    return res;
}

void measure_linear(size_t start, size_t stop, size_t step) {
    size_t tries = 200;

    std::ofstream dist("../measure_linear.log");

    std::ofstream dist2("../measure_linear_two_threads.log");

    std::cout << "| Размер корпуса | Время (в мс) без потоков | Время (в мс) с одним потоком |" << std::endl;

    for (size_t size = start; size < stop; size += step) {
        auto arr = generate_array(size, 10);
        auto start = std::clock();
        for (int i = 0; i < tries; ++i)
            get_closest_words(arr, "bbbbb", 5, 3);
        auto stop = std::clock();

        double res_time_without_mt = (double) (stop - start) / (CLOCKS_PER_SEC) / tries * 1e3;

        start = std::clock();
        for (int i = 0; i < tries; ++i)
            get_closest_words_mt(arr, "bbbbb", 5, 3, 1);
        stop = std::clock();

        double res_time_with_mt = (double) (stop - start) / (CLOCKS_PER_SEC) / tries * 1e3;

        dist << res_time_without_mt << std::endl;
        dist2 << res_time_with_mt << std::endl;
        printf("|%16zu|%26.3lf|%30.3lf|\n", size, res_time_without_mt, res_time_with_mt);
    }
}

void measure_time_with_threads(size_t thread_start, size_t thread_stop, size_t factor) {

    size_t tries = 200;
    auto arr = generate_array(10000, 10);

    std::ofstream dist("../measure_thread.log");

    std::cout << "| Количество потоков | Время (в мс) |" << std::endl;

    for (size_t tc = thread_start; tc < thread_stop; tc += factor) {
        auto start = std::clock();
        for (int i = 0; i < tries; ++i)
            get_closest_words_mt(arr, "bbbbb", 5, 3, tc);
        auto stop = std::clock();

        double res_time = (double) (stop - start) / (CLOCKS_PER_SEC) / tries * 1e3;
        dist << res_time << std::endl;
        printf("|%20zu|%14.3lf|\n", tc, res_time);
    }

    std::ofstream dist2("../measure_one_thread.log");

    auto start = std::clock();
    for (int i = 0; i < tries; ++i)
        get_closest_words(arr, "bbbbb", 5, 3);
    auto stop = std::clock();

    double res_time = (double) (stop - start) / (CLOCKS_PER_SEC) / tries * 1e3;
    dist2 << res_time << std::endl;
    std::cout << res_time << std::endl;
}