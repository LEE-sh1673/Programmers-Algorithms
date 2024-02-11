"""
우선순위:
0. 진행 중인 과제
1. 현 시각에 새로 시작해야 하는 과제 
2. 잠시 멈춰둔 과제
    - 여러 개일 경우, 가장 최근에 멈춘 과제
3. 아직 시작이 안된 과제

과제를 끝낸 순서대로 이름을 배열에 담아 return
"""
from collections import deque


def convert(time):
    hours, minutes = time.split(':')
    return int(hours) * 60 + int(minutes)


def solution(plans):    
    plans = [(name, convert(start), int(playtime))
        for name, start, playtime 
        in plans
    ]
    plans.sort(key=lambda plan: plan[1])
    que = deque()
    answer = []
    
    for idx, plan in enumerate(plans):
        name, now_time, play_time = plan
        
        if idx == len(plans) - 1:
            answer.append(name)
        else:
            que.appendleft((name, play_time))
            next_time = plans[idx+1][1]
            remain_time = next_time - now_time
            
            while que and remain_time > 0:
                recent_name, recent_remain_time = que.popleft()
                spend_time = min(remain_time, recent_remain_time)
                
                if spend_time == recent_remain_time:
                    answer.append(recent_name)
                else:
                    que.appendleft((recent_name, recent_remain_time - spend_time))
                remain_time -= spend_time
    
    while que:
        answer.append(que.popleft()[0])
    
    return answer
