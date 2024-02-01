"""
d >= sqrt((ak)^2 + (bk)^2)
d^2 >= (ak)^2 + (bk)^2
...
: b = sqrt(d^2 - (ak)^2) / k
"""
from math import sqrt


def solution(k, d):
    answer = 0
    
    # for ak (a = 0,1,2,3)
    for ak in range(0, d+1, k):
        answer += int(sqrt(d**2 - ak**2)) // k + 1
        
    return answer
