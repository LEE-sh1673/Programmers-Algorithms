from sys import stdin

limit: int = 1000000
d: list = [0, 1, 2, 4] + [0] * (limit - 3)

for i in range(4, limit + 1):
    d[i] = (d[i - 1] + d[i - 2] + d[i - 3]) % 1000000009


def sol(nums) -> list:
    return [d[num] for num in nums]


print('\n'.join(map(str, sol(map(int, stdin.readlines()[1:])))))
