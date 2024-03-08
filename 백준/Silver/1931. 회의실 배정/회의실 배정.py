n = int(input())
meetings = [list(map(int, input().split())) for _ in range(n)]
meetings.sort(reverse=True)
answer = 1
curr = meetings[0]

for i in range(1, n):
    start, end = meetings[i]
    
    if end <= curr[0]:
        answer += 1
        curr = meetings[i]

print(answer)
