"""
- 상하 이동은 답이 정해져 있음
- 중요한 점은 좌우 이동의 값을 최소로 하는 방법을 찾는 것이다.
    - 좌우 이동시 남은 문자가 모두 A 뿐이라면 더 이상 진행하지 않아도 된다.
    - 진행 중 반대 방향으로 한번 꺽는 상황이 발생할 수 있다. (이때 2번 꺽는 경우는 비효율적, 따라서 발생 X)
        1. 우로 진행, 좌로 꺽는 경우
        2. 좌로 진행, 우로 꺽는 경우
    - 그렇다면 어느 지점을 기준으로 위 2가지 경우를 비교할 수 있을까?
    - 기준이 명확하지 않기 때문에 문자열 절반 크기까지 계속 기준값으로 대입해보며 최소값을 찾는다.

e.g.JAN

1번째 문자가 기준: ('J'AN)
l -> r: J / AN
r -> l: J / NA

2번째 문자가 기준: (J'A'N)
l -> r: NJ / A
r -> l: AJ / N
"""
def solution(name):
    if set(name) == {'A'}:
        return 0

    answer = float('inf')

    for i in range(len(name)//2):
        l_r = name[-i:] + name[:-i] #왼쪽먼저 갔다가 + 오른쪽
        r_l = name[i::-1] + name[i+1:][::-1] # 기준점에서 빠꾸 + 좌측
        
        for n in [l_r,r_l]:
            while n and n[-1] == 'A':
                n = n[:-1]
            
            # 상하 최소 이동량
            min_up_down = sum([min(c-65, 91-c) for c in map(ord, n)])
            
            # 좌우 최소 이동량 
            min_side = i + len(n) - 1
            
            answer = min(answer, min_up_down + min_side)
            
    return answer
