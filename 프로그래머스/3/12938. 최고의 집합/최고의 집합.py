def solution(n, s):   
    answer = [(s+i)//n for i in range(n)]
    return answer if answer[0] else [-1]
