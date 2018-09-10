from  __future__ import print_function
import os
import sys
from string import ascii_lowercase

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    words = set(word)
    lookup = dict(zip(list(ascii_lowercase), h))
    height = 0
    for w in words:
        height = max([height, lookup[w]])
    return height * len(word)

if __name__ == '__main__':
    f = open('./input.txt')
    h = list(map(int, f.readline().rstrip().split()))
    word = f.readline().strip()
    result = designerPdfViewer(h, word)
    print(str(result))
