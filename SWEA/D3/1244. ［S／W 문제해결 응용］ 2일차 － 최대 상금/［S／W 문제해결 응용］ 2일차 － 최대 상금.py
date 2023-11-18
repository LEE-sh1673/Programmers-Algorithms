def dfs(start, cnt):
    global answer
    global visited

    if cnt == nums_change:
        answer = max(answer, int(''.join(score)))
        return
    for i in range(len(score)):
        for j in range(i + 1, len(score)):
            score[i], score[j] = score[j], score[i]
            tmp = ''.join(score)

            if (tmp, cnt) not in visited:
                visited[(tmp, cnt)] = True
                dfs(i, cnt + 1)
                
            score[i], score[j] = score[j], score[i]


for test_case in range(1, int(input()) + 1):
    score, nums_change = input().split()
    nums_change = int(nums_change)
    score = [ch for ch in score]
    answer = 0
    visited = {}
    dfs(0, 0)
    print(f'#{test_case} {answer}')