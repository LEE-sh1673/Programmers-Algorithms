def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        que = list(skill)

        for s in skill_tree:
            if s in skill and s != que.pop(0):
                break
        else:
            answer += 1
        
    return answer