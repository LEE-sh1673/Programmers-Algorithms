from sys import stdin

input = stdin.readline


def solution(nums):
    if len(nums) == m:
        print(" ".join(map(str, nums)))
        return
   
    for i in range(n):
        if visited[i]:
            continue
        
        visited[i] = True
        nums.append(numbers[i])
        solution(nums)
        visited[i] = False
        nums.pop()

n, m = map(int, input().split())
numbers = [int(num) for num in input().split()]
visited = [False] * n
numbers.sort()
solution([])
