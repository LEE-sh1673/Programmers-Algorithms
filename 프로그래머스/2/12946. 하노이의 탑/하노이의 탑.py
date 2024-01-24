"""
n = 2, A, B, C

1. A를 B로 이동
2. B를 C로 이동
3. A를 C로 이동

n = 3, A, B, C

1. A를 
"""
def solution(n):
    answer = []
    
    def hanoi(n, start, dest, via):
        nonlocal answer

        if n == 1:
            answer.append([start, dest])
        else:
            hanoi(n-1, start, via, dest)
            answer.append([start, dest])
            hanoi(n-1, via, dest, start)
    
    hanoi(n, 1, 3, 2)
    return answer
