from math import factorial


def solution(n, k):
    people = list(range(1, n+1))
    factorials = [factorial(i) for i in range(n-1, 0, -1)]
    answer = []
    
    for denom in factorials:
        q = (k - 1) // denom
        answer.append(people.pop(q))
        k %= denom
        
    return answer + people
