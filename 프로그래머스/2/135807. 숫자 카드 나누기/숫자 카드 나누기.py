"""
철수가 [10, 20]
영희가 [5, 17]

조건1
- 숫자 10으로 철수가 가진 숫자를 모두 나눌 수 있음
- 반면 영희가 가진 숫자는 하나도 나눌 수 없음

조건1에 만족하므로 현재 가장 큰 양의 정수 a는 10

이후로 두 조건 중 하나라도 만족하는 숫자가 없기 때문에 결과값은 10이 된다.

철수가 [10, 17]
영희가 [5, 20]

조건1과 조건2에 만족하는 양의 정수가 존재하지 않으므로 결과값은 0이 된다.

분석
- 두 조건 중 하나를 만족하는 가장 큰 양의 정수 a의 값을 구하기
- 조건을 만족하는 a가 없다면, 0
- arrayA와 arrayB에는 중복된 원소가 있을 수 있음
    - 중복된 원소가 존재하는 경우, 조건에 만족하는 경우가 없기 때문에 답은 0이 됨

풀이
- 
"""
from functools import reduce
import math


def gcd(arr):
    return reduce(lambda acc, el: math.gcd(acc, el), arr, 0)


def solution(arrayA, arrayB):    
    arrayA, arrayB = list(set(arrayA)), list(set(arrayB))

    answer = 0
    key_a = gcd(arrayA)
    key_b = gcd(arrayB)
    
    if all(item % key_a != 0 for item in arrayB):
        answer = key_a
    
    if all(item % key_b != 0 for item in arrayA):
        answer = max(answer, key_b)
    
    return answer
