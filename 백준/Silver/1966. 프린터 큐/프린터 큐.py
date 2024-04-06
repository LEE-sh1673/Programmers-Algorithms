from sys import stdin
from collections import deque


input = stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    que = deque(list(enumerate(nums)))
    rank_stk = sorted(nums)
    order = [0] * n
    cnt = 1
    
    while que and rank_stk:
        idx, val = que.popleft()
        
        if val < rank_stk[-1]:
            que.append((idx, val))
        else:
            rank_stk.pop()
            order[idx] = cnt
            cnt += 1
        
    print(order[m])
