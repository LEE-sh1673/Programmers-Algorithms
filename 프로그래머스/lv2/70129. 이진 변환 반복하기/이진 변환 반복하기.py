def solution(s):
    transforms, removals = 0, 0

    while s != '1':
        removals += (len(s) - s.count('1'))
        s = bin(s.count('1'))[2:]
        transforms += 1

    return [transforms, removals]
