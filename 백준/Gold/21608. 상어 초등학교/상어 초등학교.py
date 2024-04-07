from sys import stdin
from collections import defaultdict

input = stdin.readline
n = int(input())
students = defaultdict(list)

for _ in range(n*n):
    student, *likes = map(int, input().split())
    students[student] = likes

chairs = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]


def assign(student):
    candidates = []
    
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            
            like_count = 0
            blank_count = 0
            
            for dir_x, dir_y in [(0,-1),(0,1),(1,0),(-1,0)]:
                dx = i + dir_x
                dy = j + dir_y

                if dx < 0 or dx > n-1 or dy < 0 or dy > n-1:
                    continue

                if chairs[dx][dy] in students[student]:
                    like_count += 1

                if chairs[dx][dy] == 0:
                    blank_count += 1
                
            candidates.append((i, j, blank_count, like_count))
    return sorted(candidates, key=lambda c: (-c[3], -c[2], c[0], c[1]))[0]


def calc_satisfaction(x, y):
    like_count = 0

    for dir_x, dir_y in [(0,-1),(0,1),(1,0),(-1,0)]:
        dx = x + dir_x
        dy = y + dir_y

        if 0 <= dx < n and 0 <= dy < n and chairs[dx][dy] in students[chairs[x][y]]:
            like_count += 1

    return 10 ** (like_count - 1) if like_count > 0 else 0
    

for student in students:
    x, y, _, _ = assign(student)
    visited[x][y] = True
    chairs[x][y] = student

print(sum([calc_satisfaction(i, j) for i in range(n) for j in range(n)]))    
