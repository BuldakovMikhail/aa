#include <iostream>
#include "levenstein.h"
#include "correcter.h"
#include "utils.h"
#include <algorithm>

int main() {
/*
    std::cout << "Hello, World!" << std::endl;

    std::cout << lev_mtr("aboba", "boba") << std::endl;
*/
    auto arr = read_words_from_file("../data/data.txt");
    std::cout << is_word_in_vec(arr, L"mama") << std::endl;
    std::cout << is_word_in_vec(arr, L"mamx") << std::endl;

    auto preds = get_closest_words(arr, L"mamx", 2, 2);

    for (int i = 0; i < preds.size(); ++i)
        std::wcout << preds[i] << std::endl;

    std::wcout << L"Parr" << std::endl;
    preds = get_closest_words_mt(arr, L"mamx", 2, 2, 5);

    for (int i = 0; i < preds.size(); ++i)
        std::wcout << preds[i] << std::endl;



/*
    std::string data = "Abc";
    std::transform(data.begin(), data.end(), data.begin(),
                   [](unsigned char c){ return std::tolower(c); });
    */
    return 0;
}
