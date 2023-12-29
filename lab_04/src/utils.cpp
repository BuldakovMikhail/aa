//
// Created by User on 08.12.2023.
//
#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <algorithm>


std::vector<std::string> read_words_from_file(const std::string &fname) {
    std::ifstream file(fname.c_str());

    if (!file.is_open())
        return {};

    std::string temp;
    std::vector<std::string> res;

    while (std::getline(file, temp)) {
        std::transform(temp.begin(), temp.end(), temp.begin(),
                       [](unsigned char c) { return std::tolower(c); });

        res.push_back(temp);
    }

    std::sort(res.begin(), res.end());

    return res;
}

void print_arr(const std::vector<std::string> &arr, bool is_capital) {
    for (const auto &word: arr) {
        auto temp = word;
        if (is_capital)
            temp[0] = toupper(temp[0]);
        std::cout << temp << std::endl;
    }

}


