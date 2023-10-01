def solution(elements):
    answer = set()
    n = len(elements)
    elements *= 2

    for i in range(1, n + 1):
        for j in range(n):
            answer.add(sum(elements[j:j+i]))
    return len(answer)