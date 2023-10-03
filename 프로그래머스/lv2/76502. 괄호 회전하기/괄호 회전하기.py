def is_valid_parens(s):
    cnt = 0
    prev = []
    
    if s[0] in ')}]':
        return False
    
    for ch in s:
        removed = False

        if ch == '(':
            cnt += 1
        elif ch == '{':
            cnt += 2
        elif ch == '[':
            cnt += 3
            
        if cnt == 0 and ch in ')}]':
            return False
              
        if ch == ')' and prev[-1] == '(':
            cnt -=1
            prev.pop()
            removed = True
        elif ch == '}' and prev[-1] == '{':
            cnt -= 2
            prev.pop()
            removed = True
        elif ch == ']' and prev[-1] == '[':
            cnt -= 3
            prev.pop()
            removed = True
            
        if cnt < 0:
            return False
        
        if not removed:
            prev.append(ch)
            
    return cnt == 0


def solution(s):
    answer = 0
    for i in range(len(s)):
        answer += 1 if is_valid_parens(s[i:] + s[:i]) else 0
    return answer