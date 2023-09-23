def solution(s):
    answer = []
    i, n = 0, len(s)

    while i < n:
        if answer and answer[-1] == s[i]:
            answer.pop()
        else:
            answer.append(s[i])
        i += 1

    return 1 if not answer else 0