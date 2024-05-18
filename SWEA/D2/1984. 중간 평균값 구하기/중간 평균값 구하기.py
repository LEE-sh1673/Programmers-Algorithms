import math

T = int(input())

for test_case in range(1, T + 1):
    nums = [int(el) for el in input().split()]
    max_val = max(nums)
    min_val = min(nums)
    cnt = 0
    total = 0
    
    for i in range(10):
        if max_val == nums[i] or min_val == nums[i]:
            continue
        total += nums[i]
        cnt += 1
    
    answer = round(total / cnt)
    print(f'#{test_case} {answer}')