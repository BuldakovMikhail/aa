//
// Created by User on 07.12.2023.
//

#include "levenstein.h"
#include "allocate.h"

int lev_mtr(const std::wstring &str1, const std::wstring &str2) {
    size_t n = str1.length();
    size_t m = str2.length();
    int **mtr = malloc_mtr(n + 1, m + 1);
    int res = 0;

    for (int i = 0; i <= n; i++)
        for (int j = 0; j <= m; j++)
            if (i == 0 && j == 0)
                mtr[i][j] = 0;
            else if (i > 0 && j == 0)
                mtr[i][j] = i;
            else if (j > 0 && i == 0)
                mtr[i][j] = j;
            else {
                int change = 0;
                if (str1[i - 1] != str2[j - 1])
                    change = 1;

                mtr[i][j] = std::min(mtr[i][j - 1] + 1,
                                     std::min(mtr[i - 1][j] + 1,
                                              mtr[i - 1][j - 1] + change));
            }

    res = mtr[n][m];
    free_mtr(mtr, n);

    return res;
}