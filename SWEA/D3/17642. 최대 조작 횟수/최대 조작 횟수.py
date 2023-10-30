T = int(input())

"""
A + P = B
A = B - P

=> P = B-A
=> 즉 B-A가 되게 하는 소수 P, 이때 최대한 많은 횟수의 조작을 통해 A와 B의 값을 같게 만들고자 함
=> 따라서 소수 중 가장 작은 소수인 2를 계속 더하고 빼면 최대 조작 횟수를 구할 수 있다.
=> e.g.
=> A = 5, B = 10, B-A= 5, 5//2 => 2
"""

for test_case in range(1, T + 1):
    A, B = map(int, input().split())
    num = B - A
    
    if num == 0:
        cnt = 0
    elif num <= 1:
        cnt = -1
    else:
        cnt = num // 2
        
    print(f'#{test_case} {cnt}')