"""
야근 피로도 = 야근 시작 시점 + (남은 일의 작업량)^2
- 1시간 동안 작업량 1만큼 처리할 수 있음
- N시간 동안 작업량 N만큼 처리 가능

N = 4인 경우:
- A. 하나의 작업(4)만 처리 => [0, 3, 3] => 3^2 + 3^2 = 18
- B. 두개의 작업(2)을 나누어 처리 => [2, 1, 3] => 2^2 + 1^2 + 3^2 = 14
- C. 세개의 작업(2, 1, 1)을 나누어 처리 => [2, 2, 2] => 2^2 + 2^2 + 2^2 = 12

N = 3인 경우, works = [1]
- 하나의 작업(1)만 처리 => [0] = 0

N = 3인 경우, works = [1, 2]
- 두개의 작업(1, 2)을 나누어 처리 => [0, 0] = 0

N = 3인 경우, works = [1, 2, 3]
- 두개의 작업(1, 2)을 나누어 처리 => [0, 0, 3] = 9
- 세개의 작업(1, 1, 1)을 나누어 처리 => [0, 1, 2] = 5

N = 3인 경우, works = [1, 2, 3, 4]
- 한개의 작업(0, 0, 0, 3)을 나누어 처리 => [1, 2, 3, 1] = 1 + 4+ 9 + 1 = 15
- 두개의 작업(1, 2, 0, 0)을 나누어 처리 => [0, 0, 3, 4] = 25
- 두개의 작업(0, 0, 1, 2)을 나누어 처리 => [1, 2, 2, 2] = 13
- 세개의 작업(1, 1, 1, 0)을 나누어 처리 => [0, 1, 2, 4] = 21
- 세개의 작업(0, 1, 1, 1)을 나누어 처리 => [1, 1, 2, 3] = 15

N = 4인 경우, works = [3, 3, 4]
- 두개의 작업(0, 1, 3)을 나누어 처리 => [3, 2, 1] => 9 + 4 + 1 = 14
- 세개의 작업(1, 1, 2)을 나누어 처리 => [2, 2, 2] = 12

N = 4인 경우, works = [3, 3, 4, 5]
- 세개의 작업(1, 1, 2, 0)을 나누어 처리 => [2, 2, 2, 5] = 37
- 세개의 작업(0, 1, 1, 2)을 나누어 처리 => [3, 2, 3, 3] = 31
- 세개의 작업(0, 0, 2, 2)을 나누어 처리 => [3, 3, 2, 3] = 31
- 세개의 작업(0, 0, 1, 3)을 나누어 처리 => [3, 3, 3, 2] = 31
- 세개의 작업(0, 0, 0, 4)을 나누어 처리 => [3, 3, 4, 1] = 35
"""
from heapq import heappop, heappush, heapify 


def solution(n, works):
    if sum(works) < n:
        return 0
    
    works = [-work for work in works]
    heapify(works)
    
    for i in range(n):
        heappush(works, heappop(works)+1) 
        
    return sum([work ** 2 for work in works])
