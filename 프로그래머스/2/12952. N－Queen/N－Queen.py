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
    pos = [0] * n
    flag_rows = [False] * n
    diagonal_len = n * 2 - 1

    # 대각선 방향1 (↗,↙)
    flag_a = [False] * diagonal_len

    # 대각선 방향2 (↖,↘)
    flag_b = [False] * diagonal_len

    def queens(i):
        nonlocal answer

        for j in range(n):
            if not flag_rows[j] and not flag_a[j + i] and not flag_b[i - j + n - 1]:
                pos[i] = j

                if i == n - 1:
                    answer += 1
                else:
                    flag_rows[j] = flag_a[j + i] = flag_b[i - j + n - 1] = True
                    queens(i + 1)
                    flag_rows[j] = flag_a[j + i] = flag_b[i - j + n - 1] = False

    queens(0)
    return answer