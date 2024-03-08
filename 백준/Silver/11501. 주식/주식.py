"""
- 주식의 가격이 하강세인 경우 구입하지 않는다.
- 주식의 가격이 전날과 크거나 같은 경우 주식을 구매한다.
- 단, 주식을 날짜 순으로 두고 최대 이익을 구하려면 O(N^2)이 소모된다.
- 이때, 주식을 날짜의 역순으로 두고 구하는 경우 최대 이익을 구하기 쉽다.
    - 주식이 현재 값을 기준으로 최초로 감소하는 지점이 현재 최대 이익을 낼 수 있는 지점이 된다.
"""
from sys import stdin


input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    prices = list(map(int, input().split()))
    answer = 0
    j = n - 1
    
    for i in range(n-2, -1, -1):
        if prices[j] > prices[i]: # 값이 감소하는 지점
            answer += prices[j] - prices[i]
        else:
            j = i
    
    print(answer)
