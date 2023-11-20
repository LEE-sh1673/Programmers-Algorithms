def solution(arr):
    answer = {0: 0, 1: 0}

    for col in arr:
        for el in col:
            answer[el] = 0

    def check(x, y, size, arr):
        for i in range(x, x + size):
            for j in range(y, y + size):
                if arr[x][y] != arr[i][j]:
                    return False
        return True

    def dfs(x, y, size, arr):
        if check(x, y, size, arr):
            answer[arr[x][y]] += 1
            return

        k = size // 2
        dfs(x, y, k, arr)
        dfs(x + k, y, k, arr)
        dfs(x, y + k, k, arr)
        dfs(x + k, y + k, k, arr)

    dfs(0, 0, len(arr), arr)
    return list(answer.values())

