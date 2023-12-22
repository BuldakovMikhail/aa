std::vector<std::wstring> full_search(
    std::map<wchar_t, std::vector<std::wstring>> &words,
    const std::wstring &word, size_t k, size_t max_errors){

    std::vector<std::wstring> res;
    size_t min = word.size();

    for (const auto &p: words){
        if (p.first != word[0]){
            auto temp = get_closest_words(p.second, word, k, max_errors);

            if (temp.second < min){
                res = temp.first;
                min = temp.second;
            }
        }
    }

    return res;
}