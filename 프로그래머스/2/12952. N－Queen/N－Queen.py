"""
8-Queen 문제 응용
이때 n <= 12

퀸이 서로를 공격할 수 있는 경우:
- 8개의 방향으로 직선 이동하는 경로에 다른 퀸이 포함되는 경우
- 자신과 같은 행에 있는 다른 퀸을 공격 가능

=> 0 ~ n 번째 열에 각각 퀸을 배치하는 경우를 재귀로 풀 수 있다.
"""
def solution(n):
    answer = 0
    
    flag_rows = [False] * n

    # 대각선 방향1 (↗,↙)
    flag_a = [False] * (n*2 - 1)

    # 대각선 방향2 (↖,↘)
    flag_b = [False] * (n*2 - 1)

    def queens(i):
        nonlocal answer

        for j in range(n):
            if flag_rows[j] or flag_a[j+i] or flag_b[i-j+n-1]:
                continue
            
            if i == n-1:
                answer += 1
            
            flag_rows[j] = flag_a[j + i] = flag_b[i - j + n - 1] = True
            queens(i + 1)
            flag_rows[j] = flag_a[j + i] = flag_b[i - j + n - 1] = False

    queens(0)
    return answer