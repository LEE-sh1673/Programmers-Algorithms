def solution(s):
    return ' '.join([jaden_case(w) for w in s.split(" ")])


def jaden_case(s):
    if not s:
        return s

    return s.capitalize()
