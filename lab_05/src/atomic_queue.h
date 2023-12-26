//
// Created by User on 25.12.2023.
//

#ifndef SRC_ATOMIC_QUEUE_H
#define SRC_ATOMIC_QUEUE_H


#include <mutex>
#include <queue>

template<class T>
class AtomicQueue {
public:
    void push(const T &value) {
        std::lock_guard<std::mutex> lock(m_mutex);
        m_queque.push(value);
    }

    void pop() {
        std::lock_guard<std::mutex> lock(m_mutex);
        m_queque.pop();
    }

    T front() {
        std::lock_guard<std::mutex> lock(m_mutex);
        return m_queque.front();
    }

    T back() {
        std::lock_guard<std::mutex> lock(m_mutex);
        return m_queque.back();
    }

    size_t size() {
        std::lock_guard<std::mutex> lock(m_mutex);
        return m_queque.size();
    }
    //int operator[]( int i ){ return m_queque[i] };
public:
    std::queue<T> m_queque;
    mutable std::mutex m_mutex;
};

#endif //SRC_ATOMIC_QUEUE_H
