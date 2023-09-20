def solution(s):
    parens = 0

    for ch in s:
        parens = parens + 1 if ch == '(' else parens - 1
    
        if parens < 0: return False

    return parens == 0