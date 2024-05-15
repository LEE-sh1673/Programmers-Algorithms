"""
16926. 배열 돌리기
"""
n, m, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]


def rot90_anticlockwise(arr, times):
    rotated = arr[::]
    for _ in range(times):
        rotated = rotated[1:] + [rotated[0]]
    return rotated


def rotate(r):
    arr = []
    for i in range(min(n, m) // 2):
        arr.clear()
        arr += board[i][i:m - i]
        arr += [board[j][m - i - 1] for j in range(i + 1, n - i)]
        arr += board[n - i - 1][i:m - i - 1][::-1]
        arr += [board[j][i] for j in range(n - i - 2, i, -1)]

        arr = rot90_anticlockwise(arr, r)

        for j in range(i, m - i):
            board[i][j] = arr.pop(0)

        for j in range(i + 1, n - i - 1):
            board[j][m - i - 1] = arr.pop(0)

        for j in range(m - i - 1, i - 1, -1):
            board[n - i - 1][j] = arr.pop(0)

        for j in range(n - i - 2, i, -1):
            board[j][i] = arr.pop(0)


rotate(r)

for i in range(n):
    for j in range(m):
        print(board[i][j], end=' ')
    print()
print()
