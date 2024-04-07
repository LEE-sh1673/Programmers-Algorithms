from sys import stdin


def bin_search(start: int, end: int, target: int) -> int | None:
    global ans

    if start > end:
        return None

    mid: int = start + ((end - start) // 2)
    total: int = sum([num - mid for num in nums if num > mid])

    if total < target:
        return bin_search(start, mid - 1, target)
    else:
        ans = mid
        return bin_search(mid + 1, end, target)


if __name__ == '__main__':
    N, M = map(int, stdin.readline().split())
    nums = list(map(int, stdin.readline().split()))

    ans: int = 0
    bin_search(0, max(nums), M)
    print(ans)
