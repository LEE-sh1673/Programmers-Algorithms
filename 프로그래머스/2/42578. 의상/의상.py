def solution(clothes):
    from collections import Counter

    # 모든 경우의 수 => (a+1) * (b+1) * ... * (n+1) - 1
    # e.g.
    # (a+1)*(b+1)*(c+1)-1 => 7
    # a, b, c, ab, bc, ca, abc
    
    c_cnt = Counter([kind for _, kind in clothes])
    answer = 1
    for v in c_cnt.values():
        answer *= (v+1)
    return answer - 1