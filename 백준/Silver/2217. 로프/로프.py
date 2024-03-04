from sys import stdin

input = stdin.readline


def solution(n, k):
    k.sort(reverse=True)
    return max([k[i] * (i + 1) for i in range(n)])


n = int(input())
k = [int(input()) for _ in range(n)]

print(solution(n, k))