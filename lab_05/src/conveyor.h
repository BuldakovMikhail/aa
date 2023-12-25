//
// Created by User on 25.12.2023.
//

#ifndef SRC_CONVEYOR_H
#define SRC_CONVEYOR_H

#include <ctime>
#include <vector>
#include <map>
#include <string>
#include "atomic_queue.h"

struct Request {
    int id;
    bool is_last;

    timespec time_start_1;
    timespec time_end_1;
    timespec time_start_2;
    timespec time_end_2;
    timespec time_start_3;
    timespec time_end_3;

    std::wstring word;
    size_t max_errors;
    size_t k;

    bool is_correct;
    std::vector<std::wstring> res;

    Request() : id(0),
                is_last(0),
                max_errors(0),
                k(0),
                is_correct(0) {};
};

void run_pipeline(AtomicQueue<Request> &start,
                  AtomicQueue<Request> &end,
                  const std::string &fname_in,
                  const std::string &fname_out);

#endif //SRC_CONVEYOR_H
