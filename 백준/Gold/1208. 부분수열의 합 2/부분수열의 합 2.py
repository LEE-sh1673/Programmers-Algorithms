from sys import stdin
from itertools import combinations

input = stdin.readline
n, s = map(int, input().split())
nums = list(map(int, input().split()))

t1 = nums[:n//2]
t2 = nums[n//2:]

t1_comb = []
for i in range(len(t1)+1):
    t1_comb += [sum(comb) for comb in combinations(t1, i)]
t1_comb.sort()

t2_comb = []
for i in range(len(t2)+1):
    t2_comb += [sum(comb) for comb in combinations(t2, i)]
t2_comb.sort(reverse=True)

lt = 0
rt = 0
res = 0
rlen = len(t2_comb)
llen = len(t1_comb)

while lt < llen and rt < rlen:
    lp, rp = t1_comb[lt], t2_comb[rt]
    total = lp + rp
    
    if total == s:
        i, j = lt, rt

        while i < llen and t1_comb[i] == lp:
            i += 1

        while j < rlen and t2_comb[j] == rp:
            j += 1

        res += (i - lt) * (j - rt)
        lt, rt = i, j
        
    elif total > s:
        rt += 1
    else:
        lt += 1

print(res - 1 if s == 0 else res)
