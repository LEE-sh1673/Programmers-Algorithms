from sys import stdin

input = stdin.readline
exprs = input().strip()
answer = 0

# 1. "-"을 기준으로 분리한다.
first_expr, *exprs = exprs.split("-")

# 2. 첫 번째 요소와 나머지 요소들로 분리한다.
answer = sum(map(int, first_expr.split("+")))

# 3. 첫 번째 요소와 제외한 나머지 요소들의 합을 구하고 -1을 곱한다.
for expr in exprs:
    answer += -1 * sum(map(int, expr.split("+")))

print(answer)
