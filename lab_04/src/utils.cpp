//
// Created by User on 08.12.2023.
//

#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <algorithm>

std::vector<std::wstring> read_words_from_file(const std::string &fname){
    std::wifstream  file(fname.c_str());

    if (!file.is_open())
        return {};

    std::wstring temp;
    std::vector<std::wstring> res;

    for(file >> temp; !file.eof(); file >> temp) {
        std::transform(temp.begin(), temp.end(), temp.begin(),
                [](unsigned char c) { return std::tolower(c); });
        res.push_back(temp);
    }

    std::sort(res.begin(), res.end());

    return res;
}

