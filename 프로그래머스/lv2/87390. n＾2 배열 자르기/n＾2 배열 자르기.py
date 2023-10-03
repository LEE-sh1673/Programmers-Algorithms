def solution(n, left, right):
    answer = []
    
    for i in range(left, right + 1):
        x = i // n
        y = i % n
        answer.append(x + 1 if x >= y else y + 1)

    return answer