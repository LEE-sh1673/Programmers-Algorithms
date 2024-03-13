def solution(n, m):
    from itertools import product
    products = map(lambda nums: " ".join(map(str, nums)), product(range(1, n+1), repeat=m))
    print(*products, sep='\n')


n, m = map(int, input().split())
solution(n, m)
