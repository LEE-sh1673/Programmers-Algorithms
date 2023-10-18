def solution(arr):
    stk = []
    
    for el in arr:
        if stk and stk[-1] == el:
            continue
        stk.append(el)
    
    return stk