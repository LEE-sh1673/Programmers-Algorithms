"""
- 연속해서 0 또는 1이 나오는 경우를 모두 센다.
- 0이 연속해서 나오는 횟수와, 1이 연속해서 나오는 횟수 중 최소값이 답이 된다.

e.g. 
11001100110011000001

- 연속된 1이 나오는 횟수: 5
- 연속된 0이 나오는 횟수: 4

답은 4
"""
nums = [int(el) for el in input()]
n = len(nums)
nums_one = 0
nums_zero = 0
j = 0

for i in range(1, n):
    if nums[j] != nums[i]:
        if nums[j] == 1:
            nums_one += 1
        else:
            nums_zero += 1
        j = i

if nums[-1] == 0:
    nums_zero += 1
else:
    nums_one += 1

print(min(nums_one, nums_zero))
