"""
- 가로가 8, 세로가 12일때 그림을 보면 (2*3)의 패턴이 4번 반복되는 모양
- 이때, (2*3)의 패턴에서 영향을 받는 그림은 (2+3-1)
- 다른 경우를 비교해보면:

    - w=2,h=3 -> 2+3-1
    - w=4,h=6 -> 4+6-2
    - w=6,h=9 -> 6+9-3
    - w=8,h=12 -> 8+12-4

: 즉, w와 h가 주어졌을 때 대각선을 그리면 영향을 받는 범위는 `w+h-gcd(w,h)`    
"""
from math import gcd


def solution(w,h):
    if w == h:
        return w**2 - h
    
    if w <= 1 or h <= 1:
        return 0
    
    return w*h - (w+h-gcd(w,h))
