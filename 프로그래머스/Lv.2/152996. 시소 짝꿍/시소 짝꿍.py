from collections import Counter
def solution(weights):
    answer = 0
    w_counter = Counter(weights)
    
    for weight, count in w_counter.items():
        if count > 0:
            answer += count * (count - 1) // 2
            answer += count * w_counter[weight*2/3]
            answer += count * w_counter[weight*2/4]
            answer += count * w_counter[weight*3/4]
    return answer
