std::vector<std::wstring> get_closest_words(const std::vector<std::wstring> &words,
                                            const std::wstring &word,
                                            size_t k,
                                            size_t max_errors){

    if (is_word_in_vec(words, word))
        return {word};

    std::vector<std::wstring> temp;
    size_t min = word.size();

    size_t errors = std::min(static_cast<size_t>(std::ceil(0.3 * word.size())), max_errors);

    for (const auto &cur_word: words){
        int dist = lev_mtr(cur_word, word);
        if (dist < min && dist <= errors){
            temp.clear();
            temp.push_back(cur_word);
            min = dist;
        }
        else if (dist == min && dist <= errors && temp.size() < k)
            temp.push_back(cur_word);
    }

    return temp;
}