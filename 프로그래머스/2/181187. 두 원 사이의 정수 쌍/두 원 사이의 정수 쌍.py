"""
(0,0) 기준 원을 그릴 때 반지름 r1, r2가 주어진다면:

x² + y² = r² 을 이용,

x = 1 일때, 가능한 범위는
    y1 = sqrt(3) = 1.73...
    y2 = sqrt(8) = 2.82...
    => 1.73.. <= y <= 2.82...
    => 여기서 y 값은 정수만 필요하므로 => 2 <= y <= 2
    => 즉 가능한 y의 개수는 2 - 2 + 1 = 1
"""
from math import sqrt, ceil, floor


def solution(r1, r2):
    answer = 0
    for num in range(1, r2):
        if num < r1:
            y1 = ceil(sqrt(r1**2 - num**2))
            y2 = int(sqrt(r2**2 - num**2))
            answer += (y2-y1) + 1
        else:
            answer += int(sqrt(r2**2 - num**2)) + 1
    return 4 * answer + 4
