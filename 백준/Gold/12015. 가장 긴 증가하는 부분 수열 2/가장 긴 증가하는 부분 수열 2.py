from sys import stdin

input = stdin.readline
n = int(input())
A = list(map(int, input().split()))


def lower_bound(arr, target):
    s, e = 0, len(arr) - 1
    while s < e:
        mid = s + (e-s) // 2

        # [10, 15, 15, 20] <- 15? -> return '1'
        if arr[mid] < target:
            s = mid + 1
        else:
            e = mid
    return s


def second_solution(A, n):
    from bisect import bisect_left
    check = []
    for i in range(n):
        if check and check[-1] >= A[i]:
            check[bisect_left(check, A[i])] = A[i]
        else:
            check.append(A[i])
    return len(check)


print(second_solution(A, n))
