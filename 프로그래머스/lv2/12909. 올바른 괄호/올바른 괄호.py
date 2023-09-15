def solution(s):
    parens = 0

    for ch in s:
        if ch == '(':
            parens += 1
        elif ch == ')':
            parens -= 1

        if parens < 0:
            break

    return parens == 0