from sys import stdin


def sub_total(nums):
    n = len(nums)
    total = 0

    if n % 2 != 0:
        total += nums[-1]

    return total + sum([max(nums[i]+nums[i+1], nums[i]*nums[i+1]) for i in range(0, n-1, 2)])
    

def solution(n):
    plus = []
    minus = []

    for i in range(n):
        num = int(input())

        if num > 0:
            plus.append(num)
        else:
            minus.append(num)

    if n == 1:
        return plus[0] if plus else minus[0]

    plus.sort(reverse=True)
    minus.sort()
    
    total_plus = sub_total(plus)
    total_minus = sub_total(minus)
    return total_plus + total_minus


input = stdin.readline
n = int(input())
print(solution(n))
