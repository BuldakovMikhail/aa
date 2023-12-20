//
// Created by User on 08.12.2023.
//

#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <thread>
#include <mutex>

#include "correcter.h"
#include "levenstein.h"


bool is_word_in_vec(const std::vector<std::wstring> &words, const std::wstring &word){
    return std::binary_search(words.begin(), words.end(), word);
}

std::vector<std::wstring> get_closest_words(const std::vector<std::wstring> &words,
                                            const std::wstring &word,
                                            size_t k,
                                            size_t max_errors){

    std::vector<std::wstring> temp;
    size_t min = word.size();

    size_t errors = std::min(static_cast<size_t>(std::ceil(0.3 * word.size())), max_errors);

    for (const auto &cur_word: words){
        int dist = lev_mtr(cur_word, word);
        if (dist < min && dist < errors){
            temp.clear();
            temp.push_back(cur_word);
            min = dist;
        }
        else if (dist == min && temp.size() < k)
            temp.push_back(cur_word);
    }

    return temp;
}

std::mutex mutex;

void compute_distance(const std::wstring &word_cor,
                      const std::wstring &word_er,
                      size_t errors,
                      size_t k,
                      size_t &min,
                      std::vector<std::wstring> &collector)
{
    int dist = lev_mtr(word_cor, word_er);

    mutex.lock();
    if (dist < min && dist < errors){
        collector.clear();
        collector.push_back(word_cor);
        min = dist;
    }
    else if (dist == min && collector.size() < k)
        collector.push_back(word_cor);
    mutex.unlock();
}


std::vector<std::wstring> get_closest_words_mt(const std::vector<std::wstring> &words,
                                                const std::wstring &word,
                                                size_t k,
                                                size_t max_errors,
                                               size_t num_threads){

    size_t min = word.size();
    size_t errors = std::min(static_cast<size_t>(std::ceil(0.3 * word.size())), max_errors);
    std::vector<std::wstring> collector;
    std::thread threads[num_threads];

    size_t l = 0;
    while (l < words.size())
    {
        for (size_t i = 0; i < num_threads; ++i) {
            threads[i] = std::thread(compute_distance,
                                     words[l],
                                     word,
                                     errors,
                                     k,std::ref(min),
                                     std::ref(collector));
            ++l;
        }

        for (size_t i = 0; i < num_threads; ++i) {
            threads[i].join();
        }
    }

    return collector;
}