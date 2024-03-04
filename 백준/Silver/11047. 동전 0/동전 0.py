"""
11047. 동전 0
"""
from sys import stdin

input = stdin.readline


def solution(n, k):
    answer = 0
    coins = [int(input()) for _ in range(n)]

    for coin in coins[::-1]:
        if coin <= k:
            answer += k // coin
            k %= coin

    return answer


n, k = map(int, input().split())
print(solution(n, k))
