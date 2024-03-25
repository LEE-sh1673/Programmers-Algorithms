from sys import stdin

input = stdin.readline
n, r, c = map(int, input().split())
cnt = 0

def traversal(x, y, size):
    global cnt

    if x == r and y == c:
        print(cnt)
        return
    elif x <= r < x+size and y <= c < y+size:
        traversal(x, y, size//2)
        traversal(x, y+size//2, size//2)
        traversal(x+size//2, y, size//2)
        traversal(x+size//2, y+size//2, size//2)
    else:
        cnt += size**2

traversal(0, 0, 2**n)
