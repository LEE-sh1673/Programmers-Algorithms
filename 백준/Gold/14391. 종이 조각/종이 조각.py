"""
14391. 종이조각

- 종이 조각은 위에서 아래, 또는 왼쪽에서 오른쪽 방향으로 수를 이어붙인다.
- 모든 숫자가 0이 아닐 경우, 1x1 크기로 종이를 자르는 방법은 정답이 될 수 없다.
- 종이 조각은 숫자를 매기는 순서가 위->아래, 왼->오로 정해져 있기 때문에 모든 경우를 고려할 필요가 없다.

e.g.
2 2
1200
3400
0000
0000

- 1. dfs(0, 0)
    - 4. dfs(0, 1)
        - 5. dfs(1, 0) => 13 + 24
- 2. dfs(0, 1)
    - 3. dfs(1, 0) => 1 + 3 + 24

"""
N, M = map(int, input().split())
board = [[0] * 5 for _ in range(5)]
visited = [[False] * 5 for _ in range(5)]
answer = 0

for i in range(N):
    numbers = input().strip()
    for j in range(M):
        board[i][j] = int(numbers[j])


def dfs(r, c):
    global answer

    if r == 4:
        total = 0

        for i in range(N):
            temp = 0
            for j in range(M):
                if visited[i][j]:
                    temp = temp * 10 + board[i][j]
                else:
                    total += temp
                    temp = 0
            total += temp

        for i in range(M):
            temp = 0
            for j in range(N):
                if not visited[j][i]:
                    temp = temp * 10 + board[j][i]
                else:
                    total += temp
                    temp = 0
            total += temp

        answer = max(answer, total)
        return

    if c == 4:
        dfs(r + 1, 0)
        return

    visited[r][c] = True
    dfs(r, c + 1)

    visited[r][c] = False
    dfs(r, c + 1)


dfs(0, 0)
print(answer)
