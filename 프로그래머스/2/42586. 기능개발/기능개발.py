"""
- 현재 작업에 대해 배포까지 남은 기간을 계산한다.
    - 93 -> 7
- 다음 작업의 배포 기간을 계산한다.
    - 30 -> 3 
- if 현재 작업 <= 다음 작업 -> 스택에 넣음
- else -> pop & 다음 작업을 스택에 넣음
"""
def rest_time(progress, speed):
    from math import ceil
    return ceil((100 - progress) / speed)
    
def solution(progresses, speeds):
    answer = []
    stk = []
    
    for progress, speed in zip(progresses, speeds):
        curr = rest_time(progress, speed)

        if stk and stk[0] < curr:
            answer.append(len(stk))
            stk.clear()
            
        stk.append(curr)

    if stk:
        answer.append(len(stk))
    
    return answer