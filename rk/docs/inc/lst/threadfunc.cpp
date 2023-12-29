std::mutex mutex;

void compute_distance(const std::vector<std::string> &words,
                      const std::string &word_er,
                      size_t errors,
                      size_t k,
                      size_t start,
                      size_t stop,
                      size_t &min,
                      std::vector<std::string> &collector) {
    for (size_t i = start; i < stop; ++i) {
        const auto word_cor = words[i];
        int dist = lev_mtr(word_cor, word_er);

        mutex.lock();
        if (dist < min && dist <= errors) {
            collector.clear();
            collector.push_back(word_cor);
            min = dist;
        } else if (dist == min && dist <= errors && collector.size() < k)
            collector.push_back(word_cor);
        mutex.unlock();
    }
}