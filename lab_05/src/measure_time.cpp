//
// Created by User on 26.12.2023.
//

#include "conveyor.h"
#include <iostream>
#include <fstream>

void getTimeResults(int start, int stop, int step, const std::vector<std::wstring> &words) {
    std::ofstream dist("../measure_linear.log");

    std::ofstream dist2("../measure_thread.log");

    std::cout << "n | Linear | Async|\n";
    for (int i = start; i < stop; i += step) {
        AtomicQueue<Request> in;
        generator(in, i, words);
        AtomicQueue<Request> out;

        AtomicQueue<Request> in2;
        generator(in2, i, words);
        AtomicQueue<Request> out2;

        run_pipeline(in, out, "../russian_words.txt", "/dev/null");
        run_pipeline_lin(in2, out2, "../russian_words.txt", "/dev/null");

        double LinearTime = getTimeQ(out2);
        double AsyncTime = getTimeQ(out);

        dist << LinearTime << std::endl;
        dist2 << AsyncTime << std::endl;


        std::cout << i << "|" << LinearTime << "|" << AsyncTime << "|" << std::endl;
    }

}