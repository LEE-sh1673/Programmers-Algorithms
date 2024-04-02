from sys import stdin
from bisect import bisect_right


def binary_search(a, x):
    i = bisect_right(a, x)
    if i != 0 and a[i - 1] == x:
        return True
    else:
        return False


N = int(stdin.readline())
A = sorted(list(map(int, stdin.readline().split())))
M = int(stdin.readline())
B = list(map(int, stdin.readline().split()))
print('\n'.join(['1' if binary_search(A, num) else '0' for num in B]))