from sys import stdin

d = {1: 0, 2: 1}


def sol(n: int) -> int:
    if n in d:
        return d[n]
    t = 1 + min(sol(n // 3) + n % 3, sol(n // 2) + n % 2)
    d[n] = t
    return t


print(sol(int(stdin.readline())))
