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
#include <map>

#include "correcter.h"
#include "levenstein.h"


bool is_word_in_vec(const std::vector<std::wstring> &words, const std::wstring &word) {
    return std::binary_search(words.begin(), words.end(), word);
}

std::pair<std::vector<std::wstring>, size_t> get_closest_words(const std::vector<std::wstring> &words,
                                                               const std::wstring &word,
                                                               size_t k,
                                                               size_t max_errors) {

    std::vector<std::wstring> temp;
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

    return {temp, min};
}

std::vector<std::wstring> full_search(std::map<wchar_t, std::vector<std::wstring>> &words,
                                      const std::wstring &word,
                                      size_t k,
                                      size_t max_errors){

    std::vector<std::wstring> res;
    size_t min = word.size();

    for (const auto &p: words){
        if (p.first != word[0]){
            auto temp = get_closest_words(p.second, word, k, max_errors);

            if (temp.second < min){
                res = temp.first;
                min = temp.second;
            }
        }
    }

    return res;
}

std::vector<std::wstring> get_closest_words_with_segmented(std::map<wchar_t, std::vector<std::wstring>> &words,
                                                           const std::wstring &word,
                                                           size_t k,
                                                           size_t max_errors){

    if (is_word_in_vec(words[word[0]], word))
        return {word};

    auto res = get_closest_words(words[word[0]], word, k, max_errors);

    std::vector<std::wstring> ans = res.first;

    if (ans.empty()){
        ans = full_search(words, word, k, max_errors);
    }

    return ans;
}


std::mutex mutex;

void compute_distance(const std::vector<std::wstring> &words,
                      const std::wstring &word_er,
                      size_t errors,
                      size_t k,
                      size_t start,
                      size_t stop,
                      size_t &min,
                      std::vector<std::wstring> &collector) {
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


std::pair<std::vector<std::wstring>, size_t> get_closest_words_mt(const std::vector<std::wstring> &words,
                                                                  const std::wstring &word,
                                                                  size_t k,
                                                                  size_t max_errors,
                                                                  size_t num_threads) {

    size_t min = word.size();
    size_t errors = std::min(static_cast<size_t>(std::ceil(0.3 * word.size())), max_errors);
    std::vector<std::wstring> collector;
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

    return {collector, min};
}

std::vector<std::wstring> full_search_mt(std::map<wchar_t, std::vector<std::wstring>> &words,
                                      const std::wstring &word,
                                      size_t k,
                                      size_t max_errors,
                                      size_t num_threads){

    std::vector<std::wstring> res;
    size_t min = word.size();

    for (const auto &p: words){
        if (p.first != word[0]){
            auto temp = get_closest_words_mt(p.second, word, k, max_errors, num_threads);

            if (temp.second < min){
                res = temp.first;
                min = temp.second;
            }
        }
    }

    return res;
}

std::vector<std::wstring> get_closest_words_with_segmented_mt(std::map<wchar_t, std::vector<std::wstring>> &words,
                                                           const std::wstring &word,
                                                           size_t k,
                                                           size_t max_errors,
                                                           size_t num_threads){

    if (is_word_in_vec(words[word[0]], word))
        return {word};

    auto res = get_closest_words_mt(words[word[0]], word, k, max_errors, num_threads);

    std::vector<std::wstring> ans = res.first;

    if (ans.empty()){
        ans = full_search_mt(words, word, k, max_errors, num_threads);
    }

    return ans;
}