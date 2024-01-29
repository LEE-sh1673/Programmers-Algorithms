def solution(numbers: list, target: int):
    answer = 0

    def dfs(total, index):
        nonlocal answer
        
        if index == len(numbers):
            if total == target:
                answer += 1
        else:
            dfs(total + numbers[index], index + 1)
            dfs(total - numbers[index], index + 1)

    t = dfs(0, 0)
    return answer