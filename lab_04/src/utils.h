//
// Created by User on 08.12.2023.
//

#ifndef SRC_UTILS_H
#define SRC_UTILS_H

#include <string>
#include <vector>

std::vector<std::wstring> read_words_from_file(const std::string &fname);

void print_arr(const std::vector<std::wstring> &arr, bool is_capital);

#endif //SRC_UTILS_H
