from collections import Counter


def solution(k, tangerine):
    total = 0
    answer = 0
    count_by_size = Counter(tangerine).values()

    for count in sorted(count_by_size, reverse=True):
        total += count
        answer += 1

        if total >= k:
            break

    return answer