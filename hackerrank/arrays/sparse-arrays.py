from  __future__ import print_function
import os
import sys
from collections import defaultdict

def matchingStrings(strings, queries):
    op = defaultdict.fromkeys(queries, 0)
    for _ in strings:
        if _ in queries:
            op[_] = op.get(_)+ 1
    return op

if __name__ == '__main__':
    f = open('input.txt')
    strings_count = int(f.readline())

    strings = []

    for _ in xrange(strings_count):
        strings_item = f.readline().strip()
        strings.append(strings_item)

    queries_count = int(f.readline())

    queries = []

    for _ in xrange(queries_count):
        queries_item = f.readline().strip()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)
    for _ in queries:
        print(res[_])
