std::vector<std::wstring> full_search_mt(
    std::map<wchar_t, std::vector<std::wstring>> &words,
    const std::wstring &word, size_t k, size_t max_errors, size_t num_threads){

    std::vector<std::wstring> res;
    size_t min = word.size();

    for (const auto &p: words){
        if (p.first != word[0]){
            auto temp = get_closest_words_mt(p.second, word, k, max_errors, num_threads);

            if (temp.second < min){
                res = temp.first;
                min = temp.second;
            }
        }
    }

    return res;
}