def dfs(idx, total):
    global count

    if idx == n:
        if total == k:
            count += 1
    else:
        dfs(idx + 1, total)
        total += nums[idx]
        dfs(idx + 1, total)


T = int(input())

for test_case in range(1, T + 1):
    n, k = input().split()
    n = int(n)
    k = int(k)
    count = 0

    nums = list(map(int, input().split()))
    dfs(0, 0)
    print(f'#{test_case} {count}')
