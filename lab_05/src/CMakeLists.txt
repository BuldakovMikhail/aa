cmake_minimum_required(VERSION 3.25)
project(src)

set(CMAKE_CXX_STANDARD 17)

add_executable(src main.cpp atomic_queue.h correcter.cpp correcter.h levenstein.cpp levenstein.h levenstein.h conveyor.cpp utils.cpp utils.h allocate.cpp measure_time.cpp measure_time.h)
target_link_libraries(src pthread)