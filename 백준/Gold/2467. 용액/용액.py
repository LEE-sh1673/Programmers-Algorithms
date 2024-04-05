from sys import stdin

input = stdin.readline
n = int(input().strip())
nums = list(map(int, input().strip().split()))

def bin_search(start, end):
    answer = nums[start], nums[end]
    max_blending = abs(nums[start] + nums[end])

    while start < end:
        blending = nums[start] + nums[end]

        if abs(blending) < max_blending:
            max_blending = abs(blending)
            answer = nums[start], nums[end]
    
        if blending < 0:
            start += 1
        else:
            end -= 1
            
    return answer
    

print(*bin_search(0, n-1))
