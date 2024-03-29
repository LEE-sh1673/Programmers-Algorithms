from sys import stdin


def solution(n, s):
    nums = list(map(int, input().split()))
    acc, answer = 0, n+1
    start = 0

    for end in range(n):
        acc += nums[end]

        while acc >= s:
            answer = min(answer, end - start + 1)
            acc -= nums[start]
            start += 1

    return 0 if answer == n+1 else answer


input = stdin.readline
n, s = map(int, input().split())
print(solution(n, s))
