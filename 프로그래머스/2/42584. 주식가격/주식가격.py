def solution(prices):
    answer = []
    n = len(prices)
    
    for i in range(n):
        sec = 0
        
        for j in range(i+1, n):        
            sec += 1
            
            if prices[i] > prices[j]:
                break
                
        answer.append(sec)
    
    return answer