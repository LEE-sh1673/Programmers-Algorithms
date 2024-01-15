from collections import Counter

pairs = [(2, 3), (2, 4), (3, 4)]

def solution(weights):
    w_counter = Counter(weights)
    answer = 0
    for weight, count in w_counter.items():
        answer += count * (count-1) // 2
        for p1, p2 in pairs:
            answer += w_counter[weight * p1 / p2] * count
    return answer
