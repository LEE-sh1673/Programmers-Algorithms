from sys import stdin


def solution(n):
    flowers = []
    min_date = 1131
    max_date = 101

    for _ in range(n):
        s_month, s_day, e_month, e_day = map(int, input().split())
        s_date, e_date = s_month * 100 + s_day, e_month * 100 + e_day
        flowers.append((s_date, e_date))
        min_date = min(min_date, s_date)
        max_date = max(max_date, e_date)
    
    if min_date > 301 or max_date < 1201:
        return 0
    
    flowers.sort(key=lambda flower: flower[1])
    start_date = 301
    answer = 0
    
    while start_date < 1201:
        next_date = start_date
    
        for i in range(n):
            if flowers[i][0] <= start_date and flowers[i][1] > next_date:
                next_date = flowers[i][1]
    
        if next_date == start_date:
            answer = 0
            break
            
        start_date = next_date
        answer += 1
    
    return answer


input = stdin.readline
n = int(input())
print(solution(n))
