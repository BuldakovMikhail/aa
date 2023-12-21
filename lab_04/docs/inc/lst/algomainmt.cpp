std::vector<std::string> get_closest_words_mt(
    const std::vector<std::string> &words, const std::string &word,
    size_t k, size_t max_errors, size_t num_threads)
{
    if (is_word_in_vec(words, word))
        return {word};

    size_t min = word.size();
    size_t errors = std::min(static_cast<size_t>(std::ceil(0.3 * word.size())), max_errors);
    std::vector<std::string> collector;
    std::thread threads[num_threads];

    size_t l = 0;
    size_t created_threads = 0;

    while (l < words.size()) {
        created_threads = 0;
        for (size_t i = 0; i < num_threads; ++i) {
            threads[i] = std::thread(compute_distance,
                words[l], word, errors, k, std::ref(min), std::ref(collector));
            ++l;
            ++created_threads;
            if (l >= words.size())
                break;
        }
        for (size_t i = 0; i < created_threads; ++i)
            threads[i].join();
    }
    return collector;
}