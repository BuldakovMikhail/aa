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
    std::cout << arr[0] << std::endl;

/*
    std::string data = "Abc";
    std::transform(data.begin(), data.end(), data.begin(),
                   [](unsigned char c){ return std::tolower(c); });
    */
    return 0;
}
