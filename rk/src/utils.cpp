//
// Created by User on 08.12.2023.
//
#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <algorithm>

#include <locale>
#include <codecvt>

#include <map>

std::vector<std::wstring> read_words_from_file(const std::string &fname) {
    std::ifstream file(fname.c_str());

    if (!file.is_open())
        return {};

    std::string temp;
    std::wstring_convert<std::codecvt_utf8_utf16<wchar_t>> converter;
    std::vector<std::wstring> res;

    while (std::getline(file, temp)){
        std::wstring wide = converter.from_bytes(temp);
        res.push_back(wide);
    }

    std::sort(res.begin(), res.end());

    return res;
}

std::map<wchar_t, std::vector<std::wstring>> get_segmented(const std::vector<std::wstring> &arr){
    std::map<wchar_t, std::vector<std::wstring>> res;
    std::wstring letters = L"абвгдежзийклмнопрстуфхцчшщъыьэюя";


    for (auto &c : letters){
        res[c] = {};
    }

    for (const auto &w : arr){
        res[w[0]].push_back(w);
    }

    return res;
}

void print_stats(const std::map<wchar_t, std::vector<std::wstring>> &dict) {
    std::wstring_convert<std::codecvt_utf8_utf16<wchar_t>> converter;
    for (const auto &p: dict) {

        std::string narrow = converter.to_bytes(p.first);
        std::cout << narrow << " : " << p.second.size() << std::endl;
    }
}

void print_arr(const std::vector<std::wstring> &arr, bool is_capital) {
    std::wstring_convert<std::codecvt_utf8_utf16<wchar_t>> converter;
    for (const auto &word: arr) {
        auto temp = word;
        if (is_capital)
            temp[0] = toupper(temp[0]);

        std::string narrow = converter.to_bytes(temp);
        std::cout << narrow << std::endl;
    }
}


