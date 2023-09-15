def solution(s):
    return ' '.join([jaden_case(w) for w in s.split(" ")])


def jaden_case(s):
    if is_empty(s):
        return s
    
    first, second = s[0], s[1:]
    return s.lower() if not first.isalpha() else first.upper() + second.lower()


def is_empty(s):
    return not s
