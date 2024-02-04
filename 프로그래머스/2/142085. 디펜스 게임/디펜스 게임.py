"""
n=7, k=3, [4, 2, 4, 5, 3, 3, 1]

방법1:
1,3,5 라운드의 공격을 무적권으로 막아내고, 2,4 라운드에 병사를 소모 

방법2:
1,3,4 라운드의 공격을 무적권으로 막아내고, 2, 5라운드에 병사를 소모

해결 X, 참고: https://school.programmers.co.kr/questions/54133

풀이:
- 우선순위 큐를 무적권을 사용하기 위한 적의 공격에 대한 후보로 사용
- 큐에 enemy[i]를 삽입함에 따라, 큐는 가장 낮은 공격력을 가지는 enemy[i]부터 pop
- 순서대로 enemy[i]를 삽입하면서, 큐의 길이가 k를 넘어가는 시점에서 가장 낮은 공격력을 가지는 요소를 삭제
- 이렇게 하면 n이 0이 될 때까지 큐의 상태는 i번째 기준으로 가장 높은 공격력을 가진 enemy[i]만 남게 된다.
"""
from heapq import heappush, heappop


def solution(n, k, enemy):
    que = []
    
    for idx, attack in enumerate(enemy):
        heappush(que, attack)
        
        if len(que) > k:
            n -= heappop(que)
            
        if n < 0:
            return idx
    
    # 주어진 모든 enemy에 대해 방어할 수 있는 경우
    return len(enemy)
