cmake_minimum_required(VERSION 3.25)
project(build)

set(CMAKE_CXX_STANDARD 11)

add_executable(build main.cpp Matrix.h Matrix.cpp algorithms.h)
