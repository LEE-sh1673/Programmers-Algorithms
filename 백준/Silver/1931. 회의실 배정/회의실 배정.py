n = int(input())
meetings = [list(map(int, input().split())) for _ in range(n)]

last_time = float('inf')
answer = 0

for start_time, end_time in sorted(meetings, reverse=True):
    if end_time <= last_time:
        last_time = start_time
        answer += 1

print(answer)
