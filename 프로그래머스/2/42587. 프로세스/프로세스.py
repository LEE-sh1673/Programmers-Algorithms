def solution(priorities, location):
    answer = 0
    q = [(idx, priority) for idx, priority in enumerate(priorities)]
    
    while True:
        curr = q.pop(0)
        
        if any(curr[1] < priority for _, priority in q):
            q.append(curr)
        else:
            answer += 1
            
            if curr[0] == location:
                return answer