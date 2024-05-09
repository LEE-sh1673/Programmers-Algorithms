"""
3273. 두수의 합

5 12 7 10 9 1 2 3 11

1 2 3 5 7 9 10 11 12

1 12 -> 13
2 12
2 11 -> 13
3 11
3 10 -> 13
5 10
5 9
5 7
7 7
"""
n = int(input())
numbers = list(map(int, input().split()))
x = int(input())

numbers.sort()
left, right = 0, n - 1
answer = 0

while left < right:
    curr = numbers[left] + numbers[right]

    if curr == x:
        answer += 1

    if curr <= x:
        left += 1
    else:
        right -= 1

print(answer)