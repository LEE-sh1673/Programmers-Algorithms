from math import sqrt, ceil


def solution(brown, yellow):
    w = max(quadratic(2, -(brown - 4), 2*yellow))
    h = yellow // w
    return [w + 2, h + 2]


def quadratic(a, b, c):
    d = (b ** 2) - (4 * a * c)
    sol1 = ceil((-b + sqrt(d)) / (2 * a))
    sol2 = ceil((-b - sqrt(d)) / (2 * a))
    return sol1, sol2