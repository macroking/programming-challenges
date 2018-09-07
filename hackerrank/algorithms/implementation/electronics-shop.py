from  __future__ import print_function
import os
import sys

def getMoneySpent(keyboards, drives, b):
    # fptr = open('./op.txt', 'w')
    keyboards = sorted(keyboards)
    drives = sorted(drives)
    op = [-1]
    for ii in keyboards:
        for jj in drives:
            tot = ii+jj
            if tot <= b :
                # fptr.write( str(ii) + " "  + str(jj) + " " +  str(tot) + "\n")
                op.append(tot)
            else:
                break
    # fptr.close()
    return max(op)


if __name__ == '__main__':
    f = open('./input.txt')
    bnm = f.readline().strip().split()
    b = int(bnm[0])
    n = int(bnm[1])
    m = int(bnm[2])
    keyboards = list(map(int, f.readline().strip().rstrip().split()))
    drives = list(map(int, f.readline().strip().rstrip().split()))
    moneySpent = getMoneySpent(keyboards, drives, b)
    print(moneySpent)
