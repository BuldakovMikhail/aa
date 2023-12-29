void device3(AtomicQueue<Request> &from, AtomicQueue<Request> &to, const std::string &fname) {
    bool is_working = true;

    while (is_working) {
        if (from.size() > 0) {
            timespec start, end;
            Request cur_request = from.front();

            if (cur_request.is_last)
                is_working = false;

            from.pop();
            start = get_time();
            print_to_file(cur_request, fname);
            end = get_time();
            cur_request.time_start_3 = start;
            cur_request.time_end_3 = end;
            to.push(cur_request);
        }
    }
}
