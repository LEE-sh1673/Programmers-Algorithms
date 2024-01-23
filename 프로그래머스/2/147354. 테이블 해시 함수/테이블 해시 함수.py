"""
hash(col, row_begin, row_end)
    1. 테이블의 튜플을 col 번째 컬럼의 값을 기준으로 오름차순 정렬
        1.1 만약 그 값이 동일하면 기본키인 첫 번째 컬럼의 값을 기준으로 내림차순 정렬
    2. 정렬된 데이터에서 S_i를 i 번째 행의 튜플에 대해 각 컬럼의 값을 i로 나눈 나머지들의 합으로 정의
        - S_i = sum(el / i for el in row[i])
    3. row_begin ≤ i ≤ row_end 인 모든 S_i를 누적하여 bitwise XOR 한 값을 해시 값으로서 반환


e.g. hash(2, 2, 3): [[2,2,6],[1,5,10],[4,2,9],[3,8,3]]
    1. 테이블의 튜플을 2번째 컬럼의 값을 기준으로 오름차순 정렬
        - [4,2,9], [2,2,6], [1,5,10], [3,8,3]
    2. 
         2 ≤ i ≤ 3:
            S_2 = (2 mod 2) + (2 mod 2) + (6 mod 2) = 0
            S_3 = (1 mod 3) + (5 mod 3) + (10 mod 3) = 4
    3. 
         S_2 XOR S_ 3 = 4
"""
from functools import reduce


def solution(data, col, row_begin, row_end):
    # 테이블의 튜플을 2번째 컬럼의 값을 기준으로 오름차순 정렬
    data = sorted(data, key=lambda x: (x[col-1], -x[0]))
    
    # row_begin ≤ i ≤ row_end 인 모든 S_i를 구합니다.
    s = [sum(el % (i+1) for el in data[i]) for i in range(row_begin-1, row_end)] 
    
    # 모든 S_i를 누적하여 bitwise XOR 한 값을 해시 값으로서 반환합니다.
    return reduce(lambda acc, el: acc ^ el, s)
