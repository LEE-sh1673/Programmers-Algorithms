def solution(sizes):
    sizes = [[max(w,h), min(w,h)] for w, h in sizes]
    return max(sizes, key=lambda x: x[0])[0] * max(sizes, key=lambda x: x[1])[1]