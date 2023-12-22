//
// Created by User on 08.12.2023.
//

#ifndef SRC_UTILS_H
#define SRC_UTILS_H

#include <string>
#include <vector>
#include <map>

std::vector<std::wstring> read_words_from_file(const std::string &fname);

void print_arr(const std::vector<std::wstring> &arr, bool is_capital);
std::map<wchar_t, std::vector<std::wstring>> get_segmented(const std::vector<std::wstring> &arr);
void print_stats(const std::map<wchar_t, std::vector<std::wstring>> &dict);
#endif //SRC_UTILS_H
