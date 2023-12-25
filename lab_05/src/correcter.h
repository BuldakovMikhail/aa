//
// Created by User on 08.12.2023.
//

#ifndef SRC_CORRECTER_H
#define SRC_CORRECTER_H

#include <vector>
#include <string>

bool is_word_in_vec(const std::vector<std::wstring> &words, const std::wstring &word);

std::vector<std::wstring> get_closest_words(const std::vector<std::wstring> &words,
                                            const std::wstring &word,
                                            size_t k,
                                            size_t max_errors);

std::vector<std::wstring> get_closest_words_mt(const std::vector<std::wstring> &words,
                                               const std::wstring &word,
                                               size_t k,
                                               size_t max_errors,
                                               size_t num_threads);

#endif //SRC_CORRECTER_H
