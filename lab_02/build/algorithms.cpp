//
// Created by User on 21.10.2023.
//

#include "algorithms.h"

template <typename Type>
Matrix<Type> classical(const Matrix<Type> &a, const Matrix<Type> &b){
    if (a[0].size() != b.size())
        return {};
    Matrix c = Matrix(a.size(), b[0].size());
    for (int i = 0; i < a.size(); ++i)
        for (int j = 0; j < b[0].size(); ++j)
            for (int k = 0; k < b.size(); ++k)
              c[i][j] += a[i][k] * b[k][j];

    return c;
}