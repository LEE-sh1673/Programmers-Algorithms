def solution(number, k):
    answer = ''
    n = len(number)
    
    for idx, ch in enumerate(number):
        if n - idx == k:
            break
        
        if ch == '9':
            answer += ch
            continue
        
        if k > 0 and any(ch < c for c in number[idx+1:idx+1+k]):
            k -= 1
            continue
        
        answer += ch

    return answer
