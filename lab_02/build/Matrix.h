//
// Created by User on 21.10.2023.
//
#include <iostream>
#include <vector>
#include <initializer_list>

#ifndef BUILD_MATRIX_H
#define BUILD_MATRIX_H

template<typename Type>
class Matrix{
private:
    std::vector<std::vector<Type>> mtr;
public:
    Matrix() = default;
    Matrix(std::initializer_list<Type> l);
    Matrix(int N, int M);
    void addEmptyRows(int N);
    void addEmptyCols(int N);
    Type &operator[](int d);
};


#endif //BUILD_MATRIX_H
