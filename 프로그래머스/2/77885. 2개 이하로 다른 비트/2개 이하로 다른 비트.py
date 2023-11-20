"""
풀이 방법:
- 주어진 수가 짝수일 경우와 홀수인 경우에 따라 다음과 같이 처리한다.

- A. 짝수인 경우
    - 주어진 함수를 만족하는 제일 작은 수는 (짝수 + 1)이다.
    - 따라서 이 경우 답은 (짝수+1) 이다.
- B. 홀수인 경우
    - 주어진 홀수에 대해 함수를 만족하는 수는 다음과 같다.
    - e.g.
        - 7 (0111) -> 11 (1011)
        - 9 (1001) -> 10 (1010)
        - 11 (1011) -> 13 (1101)
        - 13 (1101) -> 14 (1110)
        - 15 (0 1111) -> 23 (1 0111)
        
    - 이때 숫자들의 규칙을 살펴보면 역순으로
      처음 '0'이 나오는 비트를 '1'로 바꾸고, 그 다음 비트가 '0'인 수임을 알 수 있다.
"""
def dec_to_bin(number):
    ans = ''
    
    while number > 0:
        ans += str(number % 2)
        number = number//2

    add_zero = 4 - (len(ans) % 4)
    ans += '0' * add_zero
    return ans[::-1]


def solution(numbers):
    answer = []
    
    for number in numbers:
        
        if number % 2 == 0:
            answer.append(number + 1)
            continue
        
        bin_num = dec_to_bin(number)
        zero_pos = len(bin_num) - bin_num[::-1].index('0') - 1
        
        # 7 (0111) -> 0 + 111 -> 1 + 011  -> 11 (1011)
        # 9 (1001) -> 10 + 0 + 1 -> 10 + 1 + 0 -> 10 (1010)
        bin_num = bin_num[:zero_pos] + '10' + bin_num[zero_pos+2:]
        answer.append(int(bin_num, 2))
        
    return answer
