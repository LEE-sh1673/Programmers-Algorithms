def solution(A, B):
    que_a = [a for a in sorted(A)]
    que_b = [b for b in sorted(B)]
    answer = 0
    
    while que_b:
        b = que_b.pop(0)
        a = que_a.pop(0)
        
        if b > a:
            answer += 1
        else:
            que_a.insert(0, a)

    return answer