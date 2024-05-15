"""
16926. 배열 돌리기
"""
from sys import stdin

input = stdin.readline
n, m, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]


def rotate(i):
    temp = board[i][i]

    for j in range(i, m - i - 1):
        board[i][j] = board[i][j + 1]

    for j in range(i, n - i - 1):
        board[j][m - i - 1] = board[j + 1][m - i - 1]

    for j in range(m - i - 1, i, -1):
        board[n - i - 1][j] = board[n - i - 1][j - 1]

    for j in range(n - i - 1, i, -1):
        board[j][i] = board[j - 1][i]

    board[i + 1][i] = temp


"""
- 총 연산 횟수는 약 `r * n//2 * {2(n + m) + C}`
- 이때 r = 1000, n,m = 300이라면 => 1,000 * 150 * 1,200 + 90,000 = 180,090,000
- 대략 실행 시간이 1초라면 연산 횟수는 약 1억번, 따라서 이 알고리즘의 경우 성공할지 실패할지 미지수이다.
- 실제로 python 3 기준으로 수행시켰을 때는 시간 초과가 나오지만, pypy3 환경에서는 테스트가 통과하는 것을 알 수 있다.
"""
for time in range(r):
    for i in range(min(n, m) // 2):
        rotate(i)

for i in range(n):
    for j in range(m):
        print(board[i][j], end=' ')
    print()
print()
