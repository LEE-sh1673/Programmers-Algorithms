def solution(priorities, location):
    answer = 0
    pr_que = [(no, p) for no, p in enumerate(priorities)]
    target = priorities[location]
    order = 1
    
    while pr_que:
        no, item = pr_que.pop(0)

        if pr_que and max(pr_que, key=lambda x: x[1])[-1] > item:
            pr_que.append((no, item))
            continue
            
        if item == target and location == no:
            answer = order
            break
        
        order += 1

    return answer
