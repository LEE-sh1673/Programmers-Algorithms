def solution(s):
    answer = ''
    
    words = s.split(" ")
    for word in words:
        answer += (word.capitalize()+" ")
    
    return answer[:-1:]