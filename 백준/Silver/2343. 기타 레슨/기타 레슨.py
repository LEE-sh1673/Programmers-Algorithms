from sys import stdin

input = stdin.readline
n, m = map(int, input().split())
lectures = list(map(int, input().split()))
max_lecture = max(lectures)
total_time = sum(lectures)

start, end = max_lecture, total_time + 1
answer = 0

while start < end:
    mid = (start + end) // 2
    blueray_count = 0
    play_time = 0
    
    for lecture in lectures:
        play_time += lecture
        
        if mid < play_time:
            blueray_count += 1
            play_time = lecture

    if blueray_count >= m:
        start = mid + 1
    else:
        end = mid

print(start)
