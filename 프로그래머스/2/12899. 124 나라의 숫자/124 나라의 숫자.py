from itertools import combinations


def solution(n):
    answer = ''
    
    t = ['4','1','2']
    
    while n:
        answer += t[n % 3]
        
        if n % 3 == 0:
            n = n // 3 - 1
        else:
            n = n // 3
    
    return answer[::-1]