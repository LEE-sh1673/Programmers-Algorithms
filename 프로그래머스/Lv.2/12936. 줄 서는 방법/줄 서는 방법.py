def solution(n, k):
    answer = []
    people = list(range(1, n+1))
    factorial = []
    
    tmp = 1
    for i in range(1, n):
        tmp *= i
        factorial.append(tmp)
    
    factorial = factorial[::-1]

    for denom in factorial:
        q = (k - 1) // denom
        idx = q % len(people)
        answer.append(people.pop(idx))
        
    answer.extend(people)
    return answer
