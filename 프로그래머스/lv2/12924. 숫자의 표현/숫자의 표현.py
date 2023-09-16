def solution(n):
    answer = 1

    if n < 2:
        return n

    for i in range(1, (n + 1) // 2 + 1):
        total = 0

        # 1 ~ 8
        # 2 ~ 8
        # 3 ~ 8
        # 4 ~ 8
        # 5 ~ 8
        # 6 ~ 8
        # 7 ~ 8
        for j in range(i, (n + 1) // 2 + 1):
            total += j

            if total >= n:
                break

        answer = answer + 1 if total == n else answer
    return answer