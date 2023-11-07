def solution(prices):
    answer = []
    
    for i in range(len(prices)):
        curr_price = prices[i]
        seconds = 0
        
        for j in range(i+1, len(prices)):
            if curr_price > prices[j]:
                seconds += 1
                break
            seconds += 1
            
        answer.append(seconds)
    
    return answer