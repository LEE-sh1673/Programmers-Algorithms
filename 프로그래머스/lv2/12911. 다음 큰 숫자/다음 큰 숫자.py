def solution(n):
    return next(i for i in range(n + 1, 1_000_001) if match_nums_one(n, i))


def match_nums_one(a, b):
    return dec_to_bin(a).count('1') == dec_to_bin(b).count('1')


def dec_to_bin(num):
    return bin(num).replace('0b', '')
