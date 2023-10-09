from functools import reduce


def solution(clothes):
    d = {}
    for cloth, category in clothes:
        d[category] = d.get(category, 0) + 1
    return reduce(lambda x, y: x * (y + 1), d.values(), 1) - 1