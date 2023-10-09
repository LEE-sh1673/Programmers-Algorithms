def solution(s):
    s = s[2:-2].split('},{')
    answer = []
    
    for tuple_str in sorted(s, key=lambda x: len(x)):
        for el in map(int, tuple_str.split(',')):        
            if el not in answer:
                answer.append(el)
            
    return answer