def solution(s):
    s = list(map(int, s.split()))
    s_min, s_max = str(min(s)), str(max(s))
    return ' '.join((s_min, s_max))