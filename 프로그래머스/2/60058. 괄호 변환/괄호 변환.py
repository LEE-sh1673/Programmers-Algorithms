# def convert(w: str) -> str:
#     if w == '' or is_balanced(w):
#         return w

#     u, v = split_uv(w)

#     if is_balanced(u):
#         return u + convert(v)

#     return '(' \
#         + convert(v) \
#         + ')' \
#         + reverse_brackets(u[1:-1])


# def is_balanced(w: str) -> bool:
#     cnt: int = 0
#     return all(
#         (cnt := cnt + 1 if ch == '(' else cnt - 1) >= 0
#         for ch in w
#     )

    
# def split_uv(w: str) -> tuple:
#     cnt: int = 0

#     for i, ch in enumerate(w):
#         cnt += 1 if ch == '(' else -1

#         if cnt == 0:
#             return w[:i+1], w[i+1:]

#     return '', ''


# def reverse_brackets(w: str) -> str:
#     table = str.maketrans("()", ")(")
#     return w.translate(table)

    
# def solution(w):
#     return convert(w)


#그대로 구현만 해주면 되는 문제.

#과정이 길어서 올바른 괄호열인지 확인하는 함수와, 
#괄호문자열을 모두 뒤집는 함수로 따로 빼주었다.


def solution(p):
    answer = ''
    if(len(p) == 0): #빈 문자열인 경우
        return p
    cnt = 0
    u , v = "", ""
    for i, bracket in enumerate(p): #두 "균형잡힌 괄호 문자열"로 분리
        if(bracket == "("):
            cnt += 1
        else:
            cnt -=1
        if(cnt == 0):
            u = p[:i+1]
            v = p[i+1:]
            break
    if(isCollectBrackets(u)): #u가 올바른 괄호 문자열이라면
        return u + solution(v)
    else: #u가 올바른 괄호 문자열이 아니라면
        return "(" + solution(v) + ")" + reverseBrackets(u[1:-1])
        
def reverseBrackets(brankets):
    reverseBrackets = ""
    for b in brankets:
        if(b == "("):
            reverseBrackets += ")"
        else:
            reverseBrackets += "("
    return reverseBrackets

        
def isCollectBrackets(u):
    cnt = 0
    for bracket in u:
        if bracket == "(": cnt += 1
        else: cnt -= 1
        if cnt < 0: return False
    return cnt == 0
                