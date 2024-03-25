from sys import stdin

n, m = map(int, stdin.readline().split())
nums1 = [list(map(int, stdin.readline().split())) for _ in range(n)]
nums2 = [list(map(int, stdin.readline().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        print(nums1[i][j] + nums2[i][j], end=' ')
    print()
