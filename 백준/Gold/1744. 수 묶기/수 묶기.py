from sys import stdin


def sub_total(nums):
    n = len(nums)
    total = 0

    if n % 2 != 0:
        total += nums[-1]

    return total + sum(\
        [max(nums[i]+nums[i+1], nums[i]*nums[i+1]) for i in range(0, n-1, 2)]\
    )


def solution(n):
    plus = []
    minus = []
    answer = 0

    for i in range(n):
        num = int(input())

        if num > 0:
            plus.append(num)
        elif num == 1:
            answer += 1
        else:
            minus.append(num)

    plus.sort(reverse=True)
    minus.sort()
    return answer + sub_total(plus) + sub_total(minus)


input = stdin.readline
n = int(input())
print(solution(n))
