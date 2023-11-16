def solution(x, y, n):
    if x == y:
        return 0
    
    curr = [x]
    temp = set()
    count = 1
    
    while curr:
        
        for num in curr:
            if num + n <= y:
                temp.add(num + n)
            if num * 2 <= y:
                temp.add(num * 2)
            if num * 3 <= y:
                temp.add(num * 3)
            
        if y in temp:
            return count
        
        count += 1
    
        curr = temp
        temp = set()    
            
    return -1

