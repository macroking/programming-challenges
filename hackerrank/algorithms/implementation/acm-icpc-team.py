from __future__ import print_function
import os
import sys

def acmTeam(topic):
    N = []
    cnt = len(topic)
    for ii in range(cnt):
        for jj in range(ii+1, cnt):
            op =  bin(int(topic[ii], 2) | int(topic[jj], 2)).count("1")
            N.append(op)
    return [max(N), N.count(max(N))]
if __name__ == '__main__':
    f = open('./input.txt')
    nm = f.readline().strip().split()
    n = int(nm[0])
    m = int(nm[1])
    topic = []

    for _ in range(n):
        topic_item = f.readline().strip()
        topic.append(topic_item)
    result = acmTeam(topic)
    print('\n'.join(map(str, result)))
