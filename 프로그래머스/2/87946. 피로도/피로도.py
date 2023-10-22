from itertools import permutations

def solution(k, dungeons):
    t = [nums_enter(k, ds) for ds in permutations(dungeons)]
    return max(t)


def nums_enter(k, dungeons):
    player = k
    nums_enter = 0
    
    for min_cost, cost in dungeons:
        if player >= min_cost:
            player -= cost
            nums_enter += 1
            
    return nums_enter
