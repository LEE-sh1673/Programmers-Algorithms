from collections import Counter


def solution(k, tangerine):
    tangerine_counter = sorted(
        Counter(tangerine).items(),
        key=lambda x: x[1],
        reverse=True
    )

    answer = 0
    nums_tangerine = 0

    for _, count in tangerine_counter:
        nums_tangerine += count
        answer += 1

        if nums_tangerine >= k:
            break

    return answer