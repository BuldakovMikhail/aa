std::vector<std::string> get_closest_words_mt(
    const std::vector<std::string> &words, const std::string &word,
    size_t k, size_t max_errors, size_t num_threads )
{
    if (is_word_in_vec(words, word))
        return {word};

    size_t min = word.size();
    size_t errors = std::min(static_cast<size_t>(std::ceil(0.3 * word.size())), max_errors);
    std::vector<std::string> collector;
    std::thread threads[num_threads];

    size_t range_step = words.size() / num_threads;
    
    for (size_t i = 0; i < num_threads; ++i) {
        if (i != num_threads - 1) {
            threads[i] = std::thread(compute_distance,
                words, word, errors, k, range_step * i,
                range_step * (i + 1), std::ref(min), std::ref(collector));
        } else
            threads[i] = std::thread(compute_distance,
                words, word, errors, k, range_step * i,
                words.size(), std::ref(min), std::ref(collector));
    }
    for (size_t i = 0; i < num_threads; ++i)
        threads[i].join();
    return collector;
}
