from sys import stdin

input = stdin.readline


def lower_bound(numbers, target):
    left, right = 0, len(numbers)
    
    while left < right:
        mid = left + (right - left) // 2

        if numbers[mid] < target:
            left = mid + 1
        else:
            right = mid
            
    return left


n = int(input())
numbers = list(map(int, input().split()))
v = sorted(set(numbers))

for number in numbers:
    print(lower_bound(v, number), end=' ')
