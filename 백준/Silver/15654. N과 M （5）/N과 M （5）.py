from sys import stdin

input = stdin.readline


def solution(n, m):
    from itertools import permutations
    numbers = [int(num) for num in input().split()]
    numbers = permutations(map(str, sorted(numbers)), m)
    print('\n'.join(list(map(' '.join, numbers))))


n, m = map(int, input().split())
solution(n, m)
