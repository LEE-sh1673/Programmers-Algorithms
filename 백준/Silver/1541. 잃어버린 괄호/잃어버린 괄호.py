"""
- 가장 처음과 마지막은 숫자, 즉 첫 번째 숫자는 무조건 양수가 나옴
- 최소값을 구하기 위해 처음 '-'를 기준으로 끊는다.
- 이후 각 그룹 별 합을 구하고 뺄셈 연산을 진행한다.

e.g. 10-20-30+40
1. '-'를 기준으로 끊기 => 10, 20, 30+40
2. 각 그룹의 합 구하기 => 10, 20, 70
3. 뺄셈 연산 진행 => 10 - 20 - 70 = -80
"""
from sys import stdin


formula = stdin.readline().split('-')
answer = sum([int(el) for el in formula[0].split('+')])

for stmt in formula[1:]:
    answer -= sum([int(el) for el in stmt.split('+')])
    
print(answer)
