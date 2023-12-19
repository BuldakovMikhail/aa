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

#endif //SRC_CORRECTER_H
