//
// Created by User on 07.12.2023.
//

#ifndef SRC_ALLOCATE_H
#define SRC_ALLOCATE_H

#include <iostream>
#include <cstdlib>

void free_mtr(int **mtr, std::size_t n);
int **malloc_mtr(std::size_t n, std::size_t m);

#endif //SRC_ALLOCATE_H
