//
// Created by User on 25.12.2023.
//

#include <queue>
#include <fstream>
#include <thread>

#include <locale>
#include <codecvt>

#include "conveyor.h"
#include "atomic_queue.h"
#include "correcter.h"
#include "utils.h"

timespec get_time() {
    timespec start;

    clock_gettime(CLOCK_REALTIME, &start);
    return start;
}


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

void print_to_file(const Request &req, const std::string &fname) {
    std::wstring_convert<std::codecvt_utf8_utf16<wchar_t>> converter;
    std::ofstream outfile;

    outfile.open(fname, std::ios_base::app); // append instead of overwrite

    std::string narrow = converter.to_bytes(req.word);
    outfile << narrow << '\t';

    for (const auto &w: req.res) {
        auto temp = w;
        std::string narrow = converter.to_bytes(temp);
        outfile << narrow << '\t';
    }
    outfile << std::endl;
}

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


void run_pipeline(AtomicQueue<Request> &start,
                  AtomicQueue<Request> &end,
                  const std::string &fname_in,
                  const std::string &fname_out) {

    auto words = read_words_from_file(fname_in);

    AtomicQueue<Request> secondQ;
    AtomicQueue<Request> thirdQ;

    std::thread t1(device1, std::ref(start), std::ref(secondQ), std::ref(words));
    std::thread t2(device2, std::ref(secondQ), std::ref(thirdQ), std::ref(words));
    std::thread t3(device3, std::ref(thirdQ), std::ref(end), fname_out);
    t1.join();
    t2.join();
    t3.join();
}