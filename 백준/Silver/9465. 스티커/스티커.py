for _ in range(int(input())):
    N = int(input())
    stickers = [[0, 0] + list(map(int, input().split())) for _ in range(2)]
    
    for i in range(2, N+2):
        stickers[0][i] += max(stickers[1][i-1], stickers[1][i-2])
        stickers[1][i] += max(stickers[0][i-1], stickers[0][i-2])

    answer = max(stickers[0][N+1], stickers[1][N+1])
    print(answer)
