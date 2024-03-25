from sys import stdin

input = stdin.readline
n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
block_count = 0
empty_count = 0

def check(x, y, n):
    global block_count, empty_count

    count = 0
    for i in range(x, x+n):
        for j in range(y, y+n):
            if maps[i][j] == 1:
                count += 1

    if count == n*n:
        block_count += 1        
    elif count == 0:
        empty_count += 1
    else:
        check(x, y, n//2)
        check(x, y+n//2, n//2)
        check(x+n//2, y, n//2)
        check(x+n//2, y+n//2, n//2)


check(0, 0, n)
print(empty_count)
print(block_count)
