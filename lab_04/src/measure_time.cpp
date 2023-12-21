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

std::vector<std::wstring> generate_array(size_t len, size_t word_size) {
    std::wstring temp(word_size, 'a');
    std::vector<std::wstring> res;

    for (int i = 0; i < len; ++i)
        res.push_back(temp);

    return res;
}


void measure_time_with_threads(size_t thread_start, size_t thread_stop, size_t thread_step) {

    size_t tries = 10;
    auto arr = generate_array(10000, 10);

    std::ofstream dist("../test.log");

    for (size_t tc = thread_start; tc < thread_stop; tc += thread_step) {
        auto start = std::clock();
        for (int i = 0; i < tries; ++i)
            get_closest_words_mt(arr, L"bbbbb", 5, 3, tc);
        auto stop = std::clock();

        dist << (double) (stop - start) / (CLOCKS_PER_SEC) / tries * 1e3 << std::endl;
        std::cout << tc << std::endl;
    }
}