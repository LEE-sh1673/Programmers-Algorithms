from sys import stdin


input = stdin.readline
n, s = map(int, input().split())
nums = list(map(int, input().split()))
lp, rp = 0, 0
total = nums[0]
length = n+1

while lp <= rp and rp < n:        
    if total < s:
        if rp < n-1:
            total += nums[rp+1]
        rp += 1
    else:
        length = min(length, rp - lp + 1)
        total -= nums[lp]
        lp += 1

print(0 if length == n+1 else length)
