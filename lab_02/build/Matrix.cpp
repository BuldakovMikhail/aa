//
// Created by User on 21.10.2023.
//

#include "Matrix.h"


template<typename Type>
Matrix<Type>::Matrix(int N, int M){
    mtr(N, std::vector<Type>(M, 0));
}

template<typename Type>
Matrix<Type>::Matrix(std::initializer_list<Type> l) {
    for (auto x: l){
        auto temp = std::vector<Type>();
        for (auto y: x){
            temp.push_back(y);
        }
        mtr.push_back(temp);
    }
}

template<typename Type>
void Matrix<Type>::addEmptyRows(int N){
    int m = mtr[0].size();
    for (int i = 0; i < N; ++i){
        mtr.push_back(std::vector<Type>(m, 0));
    }
}

template<typename Type>
void Matrix<Type>::addEmptyCols(int N) {
    int n = mtr.size();
    for (int i = 0; i < n; ++i){
        for (int j = 0; j < N; ++j){
            mtr[i].push_back(0);
        }
    }
}

template<typename Type>
Type &Matrix<Type>::operator[](int d) {
    return mtr[d];
}