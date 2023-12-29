cmake_minimum_required(VERSION 3.25)
project(src)

set(CMAKE_CXX_STANDARD 11)

add_executable(src main.cpp levenstein.cpp levenstein.h allocate.cpp utils.cpp utils.h correcter.cpp)
target_link_libraries(src pthread)