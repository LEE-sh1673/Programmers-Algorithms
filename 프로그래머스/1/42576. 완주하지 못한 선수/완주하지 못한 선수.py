def solution(participant, completion):
    from collections import Counter
    
    p_cnt = Counter(participant)
    
    for c in completion:
        p_cnt[c] -= 1
    
    return [name for name, cnt in p_cnt.items() if cnt != 0][0]
