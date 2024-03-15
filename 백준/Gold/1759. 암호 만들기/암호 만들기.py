from sys import stdin

input = stdin.readline


def solution(l, c):
    visited = [False] * c
    words = input().split()
    words.sort()

    def is_candidate(pwd):
        vowels = len([ch for ch in pwd if ch in 'aeiou'])
        return vowels > 0 and (l - vowels) >= 2

    def dfs(start, pwd):
        if len(pwd) == l and is_candidate(pwd):
            print(pwd)
            return

        for i in range(start, c):
            if visited[i] or (pwd and pwd[-1] >= words[i]):
                continue

            visited[i] = True
            dfs(start + 1, pwd + words[i])
            visited[i] = False

    dfs(0, '')


l, c = map(int, input().split())
solution(l, c)
