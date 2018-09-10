from __future__ import print_function
import os
import sys


def climbingLeaderboard(scores, alice):
    op = []
    scores = set(scores)
    scores = list(scores)
    scores = sorted(scores)
    max_rank = len(scores)
    cnt = 0
    for ascore in alice:
        if ascore > scores[max_rank-1]:
            op.append(1)
            continue
        if ascore < scores[0]:
            op.append(max_rank+1)
            continue
        for score in range(cnt, len(scores)):
            cnt += 1
            if ascore < scores[score]:
                op.append(max_rank+2 - cnt)
                cnt -= 1
                break
            elif ascore == scores[score]:
                op.append(max_rank+1 - cnt)
                cnt -= 1
                break
    return op


if __name__ == '__main__':
    f = open('./input.txt')
    scores_count = int(f.readline().strip())
    scores = list(map(int, f.readline().strip().rstrip().split()))
    alice_count = int(f.readline().strip())
    alice = list(map(int, f.readline().strip().rstrip().split()))
    result = climbingLeaderboard(scores, alice)
    print('\n'.join(map(str, result)))
