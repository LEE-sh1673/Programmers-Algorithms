"""
1 1
1 1


시작 지점 찾기 (0, 0)
확장하기:
    - 현재 위치를 기준으로 왼쪽/아래 쪽으로 1칸씩 확장하기
        e.g. 
            x = 0, y = 0, n = 1
                -> arr[x+n][i] (i = 0 ~ n)
                -> arr[x+n][x+n] == 1
                -> arr[i][x+n] (i = 0 ~ n)
                
            => 일치할 경우, (n + 1) ** 2 = 4
            
            x = 0, y = 0, n = 2
                -> arr[x+n][i] (i = 0 ~ n)
                -> arr[x+n][x+n] == 1
                -> arr[i][x+n] (i = 0 ~ n)
            
                -> (0, 2) == 1 ?
                -> (1, 2) == 1 ?
                -> (2, 0) == 1 ?
                -> (2, 1) == 1 ?
                -> (2, 2) == 1 ?
    - 아닐 경우 탐색을 종료하기
"""
def solution(board):
    if all(el == 0 for col in board for el in col):
        return 0
    
    answer = 1
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
                answer = max(answer, board[i][j])
    return answer ** 2;
