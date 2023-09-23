def solution(brown, yellow):
    br = brown + yellow

    for w in range(2, br + 1):
        h = br // w

        if (w - 2) * (h - 2) == yellow:
            return sorted([w, h], reverse=True)
