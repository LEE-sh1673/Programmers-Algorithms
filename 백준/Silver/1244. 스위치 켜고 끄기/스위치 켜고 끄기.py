"""
1229. 스위치 켜고 끄기

- 1이상 스위치 개수 이하인 자연수를 하나씩 지급
- 학생들은 자신의 성별과 받은 수에 따라 아래와 같은 방식으로 스위치를 조작하게 된다.

- 남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다. 즉, 스위치가 켜져 있으면 끄고, 꺼져 있으면 켠다.
- 남학생이 3을 받았다면, 이 학생은 3번, 6번 스위치의 상태를 바꾼다.

- 여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 <좌우가 대칭>이면서 <가장 많은 스위치를 포함>하는 구간을 찾아서,
- 그 구간에 속한 스위치의 상태를 모두 바꾼다. 이때 구간에 속한 스위치 개수는 항상 홀수가 된다.
- 즉 특정 스위치를 중심으로 1->3->5->7->..의 개수가 나올 수 밖에 없음

[입력]
- 스위치의 개수 N (<= 100)
- 각 스위치의 상태
- 학생 수 K
- 성별, 받은 수 (1=남, 2=여)
"""
N = int(input())
bulbs = [-1] + list(map(int, input().split()))
K = int(input())

for _ in range(K):
    sex, no = map(int, input().split())

    if sex == 1:  # 남자
        for i in range(no, N + 1, no):
            bulbs[i] = (bulbs[i] + 1) % 2

    else:  # 여자
        bulbs[no] = (bulbs[no] + 1) % 2
        left, right = no - 1, no + 1

        while left >= 0 and right < N + 1 and bulbs[left] == bulbs[right]:
            bulbs[left] = (bulbs[left] + 1) % 2
            bulbs[right] = (bulbs[right] + 1) % 2
            left -= 1
            right += 1
        
            
for i in range(1, N + 1):
    print(bulbs[i], end=" ")
    
    if i % 20 == 0:
        print()
