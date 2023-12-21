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


bool is_word_in_vec(const std::vector<std::string> &words, const std::string &word) {
    return std::binary_search(words.begin(), words.end(), word);
}

std::vector<std::string> get_closest_words(const std::vector<std::string> &words,
                                           const std::string &word,
                                           size_t k,
                                           size_t max_errors) {

    if (is_word_in_vec(words, word))
        return {word};


    std::vector<std::string> temp;
    size_t min = word.size();

    size_t errors = std::min(static_cast<size_t>(std::ceil(0.3 * word.size())), max_errors);

    for (const auto &cur_word: words) {
        int dist = lev_mtr(cur_word, word);
        if (dist < min && dist <= errors) {
            temp.clear();
            temp.push_back(cur_word);
            min = dist;
        } else if (dist == min && dist <= errors && temp.size() < k)
            temp.push_back(cur_word);
    }

    return temp;
}

std::mutex mutex;

void compute_distance(const std::vector<std::string> &words,
                      const std::string &word_er,
                      size_t errors,
                      size_t k,
                      size_t start,
                      size_t stop,
                      size_t &min,
                      std::vector<std::string> &collector) {
    for (size_t i = start; i < stop; ++i) {
        const auto word_cor = words[i];
        int dist = lev_mtr(word_cor, word_er);

        mutex.lock();
        if (dist < min && dist <= errors) {
            collector.clear();
            collector.push_back(word_cor);
            min = dist;
        } else if (dist == min && dist <= errors && collector.size() < k)
            collector.push_back(word_cor);
        mutex.unlock();
    }

}


std::vector<std::string> get_closest_words_mt(const std::vector<std::string> &words,
                                              const std::string &word,
                                              size_t k,
                                              size_t max_errors,
                                              size_t num_threads) {

    if (is_word_in_vec(words, word))
        return {word};


    size_t min = word.size();
    size_t errors = std::min(static_cast<size_t>(std::ceil(0.3 * word.size())), max_errors);
    std::vector<std::string> collector;
    std::thread threads[num_threads];

    size_t range_step = words.size() / num_threads;
    
    for (size_t i = 0; i < num_threads; ++i) {
        if (i != num_threads - 1) {
            threads[i] = std::thread(compute_distance,
                                     words,
                                     word,
                                     errors,
                                     k, range_step * i, range_step * (i + 1), std::ref(min),
                                     std::ref(collector));
        } else
            threads[i] = std::thread(compute_distance,
                                     words,
                                     word,
                                     errors,
                                     k, range_step * i, words.size(), std::ref(min),
                                     std::ref(collector));
    }

    for (size_t i = 0; i < num_threads; ++i) {
        threads[i].join();
    }

    return collector;
}