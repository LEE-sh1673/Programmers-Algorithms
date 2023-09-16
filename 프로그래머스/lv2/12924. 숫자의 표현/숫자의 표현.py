def solution(n):
    answer = 0
    
    if n < 2:
        return n
    
    k = (n + 1) // 2 + 1
    
    for i in range(1, k):
        total = 0

        for j in range(i, k):
            total += j

            if total >= n:
                break

        answer = answer + 1 if total == n else answer
    return answer + 1