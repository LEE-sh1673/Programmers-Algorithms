"""
타겟 넘버
https://school.programmers.co.kr/learn/courses/30/lessons/43165
"""


def solution(numbers: list, target: int):
    answer = 0

    def dfs(r, index):
        if index == len(numbers):
            if r == target:
                nonlocal answer
                answer += 1
        else:
            dfs(r + numbers[index], index + 1)
            dfs(r - numbers[index], index + 1)

    dfs(0, 0)
    return answer
