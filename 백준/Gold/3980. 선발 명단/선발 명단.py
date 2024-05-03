"""
3980. 선발 명단
"""
N = 11


def dfs(idx, total):
    global answer
    
    if idx == N:
        answer = max(answer, total)
        return

    for i in range(N):
        if not visited[i] and board[idx][i] != 0:
            visited[i] = True
            dfs(idx + 1, total + board[idx][i])
            visited[i] = False


for _ in range(int(input().strip())):
    board = [[int(el) for el in input().split()] for _ in range(N)]
    visited = [False] * N
    answer = -1
    dfs(0, 0)
    print(answer)
