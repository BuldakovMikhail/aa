std::vector<std::wstring> get_closest_words_with_segmented(
    std::map<wchar_t, std::vector<std::wstring>> &words, 
    const std::wstring &word, size_t k, size_t max_errors){
        
    if (is_word_in_vec(words[word[0]], word))
        return {word};

    auto res = get_closest_words(words[word[0]], word, k, max_errors);

    std::vector<std::wstring> ans = res.first;

    if (ans.empty()){
        ans = full_search(words, word, k, max_errors);
    }

    return ans;
}