"""
1. 두 큐에 담긴 모든 원소의 합을 구한다.
2. 모든 원소의 합의 절반을 탐색 목표로 세운다.
3. 다음 과정을 수행하여 탐색한다.
    1. queue1에서 숫자를 하나 추출하여 queue2에 집어넣는다.
    2. queue2에서 숫자를 하나 추출하여 queue1에 집어넣는다.
"""
from collections import deque


def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    tot1 = sum(queue1)
    tot2 = sum(queue2)
    total = tot1 + tot2

    if total % 2 != 0:
        return -1
    
    limit = (len(queue1)) * 4
    answer = 0

    while True:
        if answer == limit:
            answer = -1
            break
        
        if tot1 > tot2:
            target = queue1.popleft()
            queue2.append(target)
            tot1 -= target
            tot2 += target
            answer += 1
            
        elif tot1 < tot2:
            target = queue2.popleft()
            queue1.append(target)
            tot1 += target
            tot2 -= target
            answer += 1
        else:
            break

    return answer
