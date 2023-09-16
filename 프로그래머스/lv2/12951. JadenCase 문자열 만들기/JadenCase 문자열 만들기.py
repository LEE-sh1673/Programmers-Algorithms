def solution(s):
    arr = s.split(' ')
    answer = []
    for a in arr:
        answer.append(a.capitalize())        
    return ' '.join(answer)
