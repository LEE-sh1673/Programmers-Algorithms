"""
양의 정수 n을 k진수로 바꾸었을 때, 아래 조건에 만족하는 소수의 개수를 구하는 문제

1. 소수 양쪽에 0이 붙어있는 경우
2. 소수 오른쪽 혹은 왼쪽에만 0이 붙어있는 경우
3. 소수 양쪽에 아무것도 없는 경우

(이때 소수 자체에 자릿수에는 0이 포함되면 안된다.)

e.g. n = 437,674 / k = 3

1. 3진수 변환 -> 211020101011 
2. 소수 찾기 -> 211/020/101/011 -> 211, 2, 11
    - 이때 찾은 수는 10진법으로 보았을 때의 소수여야 한다.
3. 개수 세기 -> 3개
"""
from string import ascii_lowercase, digits
from math import sqrt

tmp = digits + ascii_lowercase

def convert(n, k):
    q, r = divmod(n, k)
    
    if q == 0:
        return tmp[r]
    else:
        return convert(q, k) + tmp[r]


def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def solution(n, k):
    # k진수 변환
    t = str(convert(n, k))
    
    # 각 나눈 숫자에서 조건에 만족하는 소수 찾기
    return sum([is_prime(int(ch, 10)) for ch in t.split('0') if ch != ''])
