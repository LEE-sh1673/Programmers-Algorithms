def dfs(cnt):
    global answer
    global visited

    if cnt == change_cnt:
        answer = max(answer, int(''.join(score)))
        return

    for i in range(n):
        for j in range(i + 1, n):
            score[i], score[j] = score[j], score[i]
            current = ''.join(score)

            if (current, cnt) not in visited:
                visited[(current, cnt)] = True
                dfs(cnt + 1)

            score[i], score[j] = score[j], score[i]


for test_case in range(1, int(input()) + 1):
    score, change_cnt = input().split()
    score = list(score)
    change_cnt = int(change_cnt)
    n = len(score)
    answer = 0
    visited = {(''.join(score), 0): True}
    dfs(0)
    print(f'#{test_case} {answer}')
