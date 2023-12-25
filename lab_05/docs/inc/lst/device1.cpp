void device1(AtomicQueue<Request> &from, AtomicQueue<Request> &to, const std::vector<std::wstring> &words) {
    bool is_working = true;

    while (is_working) {
        if (from.size() > 0) {
            timespec start, end;
            Request cur_request = from.front();

            if (cur_request.is_last)
                is_working = false;

            from.pop();

            start = get_time();
            if (is_word_in_vec(words, cur_request.word))
                cur_request.is_correct = true;
            end = get_time();

            cur_request.time_start_1 = start;
            cur_request.time_end_1 = end;
            to.push(cur_request);
        }

    }
}
