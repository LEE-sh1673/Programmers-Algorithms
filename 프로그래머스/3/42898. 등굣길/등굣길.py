'''
첫 번째 풀이: (시간 초과)
1. 아래 조건에 만족할 경우 탐색을 종료한다.
    - (x, y) == (m, n):
        - 현재 경로 cost == 현재 최단 경로:
            - 최단 경로 개수 += 1
        - 현재 경로 cost < 현재 최단 경로:
            - 최단 경로 개수 = 1
            - 현재 최단 경로 = 현재 경로 cost
2-1. 아래 이동
    - 이동이 불가능한 경우 넘어간다.
        - 물에 잠긴 경우
        - 이동이 불가능한 경우
    - 이동이 가능한 경우
        - func(x, y+1, cnt + 1, puddles)
2-2. 오른쪽 이동
    - 이동이 불가능한 경우 넘어간다.
    - 이동이 가능한 경우
        - func(x + 1, y, cnt + 1, puddles)
        
두 번째 풀이:
- 다음 점화식을 적용
- dp[x][y] = dp[x-1][y] + dp[x][y-1]
- 이때 전처리 과정으로 puddles의 좌표를 미리 0으로 처리
'''

def solution(m, n, puddles):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 1
    
    for x in range(n):
        for y in range(m):
            if [y+1, x+1] in puddles:
                continue
                
            if x - 1 >= 0:
                dp[x][y] += dp[x-1][y]
            if y - 1 >= 0:
                dp[x][y] += dp[x][y-1]  
    
    return dp[n-1][m-1] % 1_000_000_007
