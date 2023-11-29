def solution(answers):
    answer = []
    n = len(answers)
    
    u1 = [1,2,3,4,5] * n
    u2 = [2,1,2,3,2,4,2,5] * n
    u3 = [3,3,1,1,2,2,4,4,5,5] * n
    cnts = [0] * 3
    
    for i in range(n):
        ans = answers[i]
        
        if ans == u1[i]:
            cnts[0] += 1
        if ans == u2[i]:
            cnts[1] += 1
        if ans == u3[i]:
            cnts[2] += 1
    
    return [idx+1 for idx, el in enumerate(cnts) if el == max(cnts)]
