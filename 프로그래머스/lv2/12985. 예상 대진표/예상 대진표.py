from math import ceil


def solution(n, a, b):
    if a == b:
        return 0

    return 1 + solution(n, ceil(a/2), ceil(b/2))