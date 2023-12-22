std::pair<std::vector<std::wstring>, size_t> get_closest_words(
    const std::vector<std::wstring> &words, const std::wstring &word,
    size_t k, size_t max_errors) {

    std::vector<std::wstring> temp;
    size_t min = word.size();

    size_t errors = std::min(static_cast<size_t>(std::ceil(0.3 * word.size())), max_errors);

    for (const auto &cur_word: words) {
        int dist = lev_mtr(cur_word, word);
        if (dist < min && dist <= errors) {
            temp.clear();
            temp.push_back(cur_word);
            min = dist;
        } else if (dist == min && dist <= errors && temp.size() < k)
            temp.push_back(cur_word);
    }

    return {temp, min};
}