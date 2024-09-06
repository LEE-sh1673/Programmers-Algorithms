def solution(answers):    
    u1 = [1,2,3,4,5]
    u2 = [2,1,2,3,2,4,2,5]
    u3 = [3,3,1,1,2,2,4,4,5,5]
    cnts = [0] * 3
    answer = []
    
    for i, ans in enumerate(answers):        
        if ans == u1[i % 5]:
            cnts[0] += 1
        if ans == u2[i % 8]:
            cnts[1] += 1
        if ans == u3[i % 10]:
            cnts[2] += 1
    
    return [idx+1 for idx, el in enumerate(cnts) if el == max(cnts)]
