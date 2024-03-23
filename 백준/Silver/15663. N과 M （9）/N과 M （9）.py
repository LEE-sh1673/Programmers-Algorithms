from sys import stdin

input = stdin.readline


def solution(n, m):
    visited = set()
    nums = list(map(int, input().split()))
    v2 = [False] * n
    nums.sort()
    
    def bt(t):    
        if len(t) == m:
            t = tuple(t)
            
            if t not in visited:
                visited.add(t)
                print(' '.join(map(str, t)))
            return

        for i in range(n):
            if not v2[i]:
                v2[i] = True
                t.append(nums[i])
                bt(t)
                v2[i] = False
                t.pop()
            
    bt([])


n, m = map(int, input().split())
solution(n, m)
