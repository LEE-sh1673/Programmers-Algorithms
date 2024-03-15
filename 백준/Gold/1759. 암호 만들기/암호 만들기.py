from sys import stdin

input = stdin.readline


def solution(l, c):
    visited = [False] * c
    words = input().split()
    words.sort()

    def is_candidate(pwd):
        v_count, c_count = 0, 0  # 모음 개수, 자음 개수

        for i in pwd:
            if i in 'aeiou':
                v_count += 1
            else:
                c_count += 1

        if v_count >= 1 and c_count >= 2:
            return True
        else:
            return False

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
