from __future__ import print_function
import os
import sys


def gridSearch(G, P):
    exists = "NO"
    max_rows = len(G)
    max_columns = len(G[0])
    exp_row = len(P)
    exp_col = len(P[0])
    op = [[False for x in range(exp_col)] for y in range(exp_row)]
    bottom = (max_rows - exp_row) + 1
    right = (max_columns - exp_col) + 1

    exp_row_ = 0
    ii = 0

    while ii < bottom:
        if op[exp_row_].count(True) == exp_row + 1:
            exp_row_ += 1
        else:
            [False for row in op[exp_row_]]

        exp_col_ = 0
        jj = 0
        while jj < right + 1:
            if exp_col_ <= exp_col - 1 and exp_row_ <= exp_row:
                if G[ii][jj] == P[exp_row_][exp_col_]:
                    op[exp_row_][exp_col_] = True
                    exp_col_ += 1
                    jj += 1
                else:
                    [False for row in op[exp_row_]]
                    if exp_col_ > 0:
                        print(ii, exp_row_, op[exp_row_])
                        jj = jj - 1
                    jj += 1
                    exp_col_ = 0
            else:
                break
        ii += 1
        print()
    if exp_row_ == exp_row:
        exists = 'YES'
    print(op)
    return exists


if __name__ == '__main__':
    f = open('./input.txt')
    t = int(f.readline().strip())
    for t_itr in range(t):
        RC = f.readline().strip().split()
        R = int(RC[0])
        C = int(RC[1])
        G = []

        for _ in range(R):
            G_item = f.readline().strip()
            G.append(G_item)

        rc = f.readline().strip().split()
        r = int(rc[0])
        c = int(rc[1])
        P = []

        for _ in range(r):
            P_item = f.readline().strip()
            P.append(P_item)

        result = gridSearch(G, P)
        print(result)
