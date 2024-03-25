def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        
    return True


def solution(numbers):
    unique_numbers = set()
    n = len(numbers)
    visited = [False] * n

    def dfs(total, idx):
        if total != "":
            num = int(total)

            if is_prime(num):
                unique_numbers.add(num)

            if idx == n:
                return

        for i, ch in enumerate(numbers):
            if not visited[i]:
                visited[i] = True
                dfs(total + ch, idx + 1)
                visited[i] = False

    dfs("", 0)
    return len(unique_numbers)