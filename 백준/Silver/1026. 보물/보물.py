from sys import stdin

input = stdin.readline
n = int(input())
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
nums1.sort()
nums2.sort(reverse=True)
print(sum([nums1[i]*nums2[i] for i in range(n)]))
