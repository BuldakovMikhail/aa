#include <iostream>
#include "utils.h"
#include <algorithm>
#include "correcter.h"

int main() {

    auto res = read_words_from_file("../russian_words.txt");

    auto seg = get_segmented(res);
    auto ans = get_closest_words_with_segmented_mt(seg, L"мамы", 2, 2, 2);

    print_arr(ans, false);
    print_stats(seg);

    return 0;
}
