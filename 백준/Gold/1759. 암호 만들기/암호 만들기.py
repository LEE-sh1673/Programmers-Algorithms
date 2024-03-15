from sys import stdin

input = stdin.readline


def solution(l, c):
    visited = [False] * c
    words = input().split()
    words.sort()

    def is_candidate(pwd):
        vowels = len([ch for ch in pwd if ch in "aeiou"])
        return vowels >= 1 and (l - vowels) >= 2

    def dfs(pwd):
        if len(pwd) == l and is_candidate(pwd):
            print("".join(pwd))
            return

        for i in range(c):
            if visited[i] or (pwd and pwd[-1] >= words[i]):
                continue

            visited[i] = True
            pwd.append(words[i])
            dfs(pwd)
            visited[i] = False
            pwd.remove(words[i])

    dfs([])


l, c = map(int, input().split())
solution(l, c)
