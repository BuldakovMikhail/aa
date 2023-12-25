#include <iostream>
#include "conveyor.h"
#include "atomic_queue.h"

int main() {
    AtomicQueue<Request> start;
    AtomicQueue<Request> end;

    Request t;
    t.id = 0;
    t.word = L"сламандр";
    t.max_errors = 5;
    t.is_last = true;
    t.k = 3;

    start.push(t);

    run_pipeline(start, end, "../russian_words.txt", "../res.txt");

    std::cout << "Hello, World!" << std::endl;
    return 0;
}
