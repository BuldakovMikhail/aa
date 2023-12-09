cmake_minimum_required(VERSION 3.25)
project(src)

set(CMAKE_CXX_STANDARD 17)

add_executable(src main.cpp levenstein.h levenstein.cpp allocate.cpp allocate.h utils.h utils.cpp correcter.cpp correcter.h)
