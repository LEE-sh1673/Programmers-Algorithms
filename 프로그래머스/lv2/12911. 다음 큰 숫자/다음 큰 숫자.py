
def solution(n):
    n_ones = nums_one(n)
    return next(i for i in range(n + 1, 2 * n + 1) if n_ones == nums_one(i))


def nums_one(num):
    return bin(num).count('1')
