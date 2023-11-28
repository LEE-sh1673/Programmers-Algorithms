def solution(number, k):    
    answer = []
    n = len(number)
    
    for i in range(n):
        while answer and k > 0 and answer[-1] < number[i]:
            answer.pop()
            k -= 1
        answer.append(number[i])    
        
    return ''.join(answer)[:n-k]
