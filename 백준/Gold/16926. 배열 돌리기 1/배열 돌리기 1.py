"""
16926. 배열 돌리기
"""
n, m, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]


def rotate(i):
    # (0, 0) -> (1, 1)
    temp = board[i][i]

    # 1. 위 (왼 <- 오) : 2 3 4 4
    for j in range(i, m - i - 1):
        board[i][j] = board[i][j + 1]

    # 2. 오 (위 <- 아래): 8 12 16 16
    for j in range(i, n - i - 1):
        board[j][m - i - 1] = board[j + 1][m - i - 1]

    # 3. 아래 (왼 -> 오): 13 13 14 15
    for j in range(m - i - 1, i, -1):
        board[n - i - 1][j] = board[n - i - 1][j - 1]

    # 4. 왼 (위 -> 아래): 2 2 5 9
    for j in range(n - i - 1, i, -1):
        board[j][i] = board[j - 1][i]

    # 5. 대체 (board[i+1][i] = temp)
    board[i + 1][i] = temp


"""
total = r * n//2 * (2n + 2m - 8i + 1)
[r = 1000, n,m = 300]
=> 1000 * 150 * (2*300 + 2*300) = 135,150,000 + 90,000
"""
for time in range(r):
    for i in range(min(n, m)//2):
        rotate(i)

for i in range(n):
    for j in range(m):
        print(board[i][j], end=' ')
    print()
print()
