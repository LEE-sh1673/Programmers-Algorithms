def solution(n):
    if n < 2:
        return n

    k = (n + 1) // 2 + 1
    answer = 0

    for i in range(1, k):
        total = 0
        j = i
        
        while total < n:
            total += j
            j += 1

        answer = answer + 1 if total == n else answer

    return answer + 1