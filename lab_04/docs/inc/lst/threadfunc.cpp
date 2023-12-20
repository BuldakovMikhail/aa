std::mutex mutex;

void compute_distance(const std::wstring &word_cor,
                      const std::wstring &word_er,
                      size_t errors,
                      size_t k,
                      size_t &min,
                      std::vector<std::wstring> &collector)
{
    int dist = lev_mtr(word_cor, word_er);

    mutex.lock();
    if (dist < min && dist < errors){
        collector.clear();
        collector.push_back(word_cor);
        min = dist;
    }
    else if (dist == min && collector.size() < k)
        collector.push_back(word_cor);
    mutex.unlock();
}