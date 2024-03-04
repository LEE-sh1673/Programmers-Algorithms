from sys import stdin

input = stdin.readline


def solution(n, k):
    k.sort(reverse=True)
    answer = 0

    for i in range(n):
        answer = max(answer, k[i] * (i+1))

    return answer


n = int(input())
k = [int(input()) for _ in range(n)]

print(solution(n, k))