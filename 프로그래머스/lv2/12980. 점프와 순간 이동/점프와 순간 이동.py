# def solution(n):
#     return bin(n).count('1')


def solution(n):
    return sum([n >> i & 1 for i in range(n.bit_length())])
