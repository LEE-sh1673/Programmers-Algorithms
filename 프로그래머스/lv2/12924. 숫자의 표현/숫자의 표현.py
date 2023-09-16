def solution(n):
    answer = 0

    for i in range(1, (n + 1) // 2 + 1):
        total = 0

        for j in range(i, (n + 1) // 2 + 1):
            total += j

            if total >= n:
                break

        answer = answer + 1 if total == n else answer
    return answer + 1