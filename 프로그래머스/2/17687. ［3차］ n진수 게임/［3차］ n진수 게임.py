import string

tmp = string.digits+string.ascii_uppercase

def convert(num, base) :
    q, r = divmod(num, base)
    
    if q == 0:
        return tmp[r] 
    else:
        return convert(q, base) + tmp[r]

def solution(n, t, m, p):
    
    # 2진법, 4개의 숫자를 말해야 함, 참여 인원 2명, 순서 1번째
    # 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 
    # (0), (1), (1, 0), (1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0)
    # 0, 1, 1, 1
    # 0111
    
    # 16진법, 16개의 숫자를 말해야 함, 참여 인원 2명, 순서 1번째
    # 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> ... -> 16 -> ... -> 21 -> ...
    # 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> ... -> A -> ... -> F -> 10 -> 11 -> 12 -> 13 -> 14 -> 15  
    # 13579BDF11
    # 0111
    
    s = '0'
    for num in range(1, m*t):
        s += convert(num, n)
    return s[p-1::m][:t]
