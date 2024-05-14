"""
17393. 다이나믹 룰러

멩미가 i 번째 타일 위에 서 있을 때, 다음 조건에 만족하는 칸을 칠할 수 있다.

1. 현재 위치 보다 오른쪽
2. 점도 지수(Bi) <= 현재 위치의 잉크 지수(Ai)
"""
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(N):
    start, end = i, N

    while start < end:
        mid = start + (end - start) // 2

        if B[mid] <= A[i]:
            start = mid + 1
        else:
            end = mid

    print(start - i - 1, end=' ')
