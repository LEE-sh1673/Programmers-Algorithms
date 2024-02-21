"""
2178. 미로 탐색
"""
from sys import stdin


def bfs(maze: list, directions: list, n: int, m: int):
    q = [(1, 1)]

    while q:
        x, y = q.pop(0)
        for dir_x, dir_y in directions:
            nx, ny = x + dir_x, y + dir_y

            if maze[nx][ny] == 1:
                q.append((nx, ny))
                maze[nx][ny] = maze[x][y] + 1

    return maze[n][m]


def main():
    n, m = map(int, stdin.readline().split())
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    maze = [[0] * (m + 2)]
    for _ in range(n):
        maze.append([0] + list(map(int, list(input()))) + [0])
    maze.append([0] * (m + 2))
    print(bfs(maze, directions, n, m))


main()
