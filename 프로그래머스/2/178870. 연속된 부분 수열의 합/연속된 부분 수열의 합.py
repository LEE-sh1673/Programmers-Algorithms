"""
완전탐색/투 포인터
"""


def solution(sequence, k):
    answer = []

    n = len(sequence)
    s, e = 0, 0
    total = 0

    while s < n:
        if total >= k:
            total -= sequence[s]
            s += 1
        else:
            if e >= n:
                break

            total += sequence[e]
            e += 1

        if total == k:
            answer.append((s, e-1))

    """
    1. 길이가 제일 짧으며
    2. 제일 먼저 나온 순
    """
    answer.sort(key=lambda x: (x[1] - x[0], x[0]))
    return [answer[0][0], answer[0][1]]