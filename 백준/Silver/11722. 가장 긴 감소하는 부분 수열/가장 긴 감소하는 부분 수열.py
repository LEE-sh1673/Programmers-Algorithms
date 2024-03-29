from sys import stdin

input = stdin.readline
n = int(input().strip())
nums = list(map(int, input().split()))
check = []
dp = [1] * n


def lower_bound(x):
    start, end = 0, len(check) - 1
    ans = 0
    
    while True:
        if start > end:
            return ans
            
        mid=(start+end)//2

        if check[mid] <= x:
            ans=mid
            end=mid-1
        else:
             start=mid+1


for i in range(n):
    if not check or check[-1] > nums[i]:
        check.append(nums[i])
    else:
        idx = lower_bound(nums[i])
        check[idx] = nums[i]
    dp[i] = len(check)

print(max(dp))
