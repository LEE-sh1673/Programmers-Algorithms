"""
1026. 보물
"""
from sys import stdin

input = stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

print(sum([a_i * b_i for a_i, b_i in zip(a, b)]))
