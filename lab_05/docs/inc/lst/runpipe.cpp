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