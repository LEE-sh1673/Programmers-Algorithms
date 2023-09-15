def solution(s):
    removals, transforms = 0, 0

    while s != '1':
        removals += (len(s) - s.count('1'))
        transforms += 1

        nums_one = s.count('1')
        s = bin(nums_one)[2:]

    return [transforms, removals]