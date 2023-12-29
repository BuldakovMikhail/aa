
void device2(AtomicQueue<Request> &from, AtomicQueue<Request> &to, const std::vector<std::wstring> &words) {
    bool is_working = true;

    while (is_working) {
        if (from.size() > 0) {
            timespec start, end;
            Request cur_request = from.front();

            if (cur_request.is_last)
                is_working = false;

            from.pop();
            start = get_time();
            if (!cur_request.is_correct)
                cur_request.res = get_closest_words(words,
                                                    cur_request.word,
                                                    cur_request.k,
                                                    cur_request.max_errors);
            end = get_time();
            cur_request.time_start_2 = start;
            cur_request.time_end_2 = end;
            to.push(cur_request);
        }
    }
}