from sys import stdin


def dfs(prev_v: int, idx: int, plus, minus, mutiply, divide):
    if idx == N:
        res.append(prev_v)
    else:
        if plus:
            dfs(prev_v + A[idx], idx + 1, plus - 1, minus, mutiply, divide)
        if minus:
            dfs(prev_v - A[idx], idx + 1, plus, minus - 1, mutiply, divide)
        if mutiply:
            dfs(prev_v * A[idx], idx + 1, plus, minus, mutiply - 1, divide)
        if divide:
            next_v: int = abs(prev_v) // A[idx] * -1 if prev_v < 0 else prev_v // A[idx]
            dfs(next_v, idx + 1, plus, minus, mutiply, divide - 1)


if __name__ == '__main__':
    N: int = int(stdin.readline())
    A: list[int] = list(map(int, stdin.readline().split()))
    ops: list[int] = list(map(int, stdin.readline().split()))
    res = []

    dfs(A[0], 1, *ops)
    print(max(res), min(res), sep='\n')
