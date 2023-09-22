def solution(n):
    n_ones = nums_one(n)
    return next(i for i in range(n + 1, 2 * n + 1) if n_ones == nums_one(i))


def nums_one(num):
    return dec_to_bin(num).count('1')


def dec_to_bin(num):
    return bin(num).replace('0b', '')
