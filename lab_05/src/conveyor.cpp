//
// Created by User on 25.12.2023.
//

#include <queue>
#include <fstream>
#include <thread>
#include <string>

#include <locale>
#include <codecvt>

#include <iostream>

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

            if (cur_request.is_last) {
                is_working = false;
                to.push(cur_request);
                break;
            }

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

            if (cur_request.is_last) {
                is_working = false;
                to.push(cur_request);
                break;
            }

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

double diff_timespec(const timespec &time1, const timespec &time0) {
    return (time1.tv_sec - time0.tv_sec)
           + (time1.tv_nsec - time0.tv_nsec) / 1000000000.0;
}

double getTimeQ(AtomicQueue<Request> &st) {
    double time = diff_timespec(st.back().time_end_3, st.front().time_start_1);
    return time;
}


void createReport(AtomicQueue<Request> &requests) {
    std::cout << "| N | Начало 1 | Конец 1 | Начало 2 | Конец 2 | Начало 3 | Конец 3 |\n";
    int requestsCount = requests.size();
    //std::cout<< requestsCount << "\n";

    /*double min_1 = 1e10;
    double min_2 = 1e10;
    double min_3 = 1e10;

    double max_1 = -1;
    double max_2 = -1;
    double max_3 = -1;

    double mean_1 = 0;
    double mean_2 = 0;
    double mean_3 = 0;*/


    timespec start = requests.front().time_start_1;
    for (int i = 0; i < requestsCount; i++) {
        Request req = requests.front();
        requests.pop();
        double started_1 = diff_timespec(req.time_start_1, start);
        double ended_1 = diff_timespec(req.time_end_1, start);

        double started_2 = diff_timespec(req.time_start_2, start);
        double ended_2 = diff_timespec(req.time_end_2, start);

        double started_3 = diff_timespec(req.time_start_3, start);
        double ended_3 = diff_timespec(req.time_end_3, start);

        std::cout << "|" << i << "|" << started_1 << "|" << ended_1 << "|" << started_2 << "|" << ended_2 << "|"
                  << started_3 << "|" << ended_3 << "|" << std::endl;
        requests.push(req);
    }
    std::cout << "Общее время: " << getTimeQ(requests) << std::endl;
}

void device3(AtomicQueue<Request> &from, AtomicQueue<Request> &to, const std::string &fname) {
    bool is_working = true;

    while (is_working) {
        if (from.size() > 0) {
            timespec start, end;
            Request cur_request = from.front();

            if (cur_request.is_last) {
                is_working = false;
                break;
            }

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

void generator(AtomicQueue<Request> &q, size_t count, const std::vector<std::wstring> &words) {
    for (size_t i = 0; i < count; ++i) {
        std::wstring word = words[std::rand() % words.size()];

        if (word.size() == 1)
            return;

        int errors = word.size() * 0.1 + 1;

        for (int j = 0; j < errors; ++j) {
            double p = std::rand() / RAND_MAX;
            if (p < 0.33) {
                int cpos = std::rand() % word.size();
                wchar_t c = word[cpos];
                if (c == L'а')
                    c += 1;
                else
                    c -= 1;

                word[cpos] = c;
            } else if (p < 0.66) {
                int pos = std::rand() % word.size();
                word.insert(word.begin() + pos, word[pos]);
            } else {
                int pos = std::rand() % (word.size() - 1);
                auto temp = word[pos];
                word[pos] = word[pos + 1];
                word[pos + 1] = temp;
            }
        }
        q.push({word, i});
    }
    q.push({});
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
    std::thread t22(device2, std::ref(secondQ), std::ref(thirdQ), std::ref(words));
    std::thread t3(device3, std::ref(thirdQ), std::ref(end), fname_out);
    t1.join();
    t2.join();
    t22.join();
    t3.join();
}

void device1_lin(AtomicQueue<Request> &from, AtomicQueue<Request> &to, const std::vector<std::wstring> &words) {

    while (from.size() > 0) {
        timespec start, end;
        Request cur_request = from.front();

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


void device2_lin(AtomicQueue<Request> &from, AtomicQueue<Request> &to, const std::vector<std::wstring> &words) {
    while (from.size() > 0) {
        timespec start, end;
        Request cur_request = from.front();
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


void device3_lin(AtomicQueue<Request> &from, AtomicQueue<Request> &to, const std::string &fname) {
    while (from.size() > 0) {
        timespec start, end;
        Request cur_request = from.front();
        from.pop();
        start = get_time();
        print_to_file(cur_request, fname);
        end = get_time();
        cur_request.time_start_3 = start;
        cur_request.time_end_3 = end;
        to.push(cur_request);
    }
}


void run_pipeline_lin(AtomicQueue<Request> &start,
                      AtomicQueue<Request> &end,
                      const std::string &fname_in,
                      const std::string &fname_out) {

    auto words = read_words_from_file(fname_in);

    AtomicQueue<Request> secondQ;
    AtomicQueue<Request> thirdQ;

    device1_lin(start, secondQ, words);
    device2_lin(secondQ, thirdQ, words);
    device3_lin(thirdQ, end, fname_out);
}