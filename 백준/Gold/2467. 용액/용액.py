from sys import stdin

input = stdin.readline
n = int(input())
juices = list(map(int, input().split()))
min_blending = abs(juices[0] + juices[-1])


def search(start, end):
    ans_x, ans_y = 0, n-1
    min_blending = abs(juices[start] + juices[end])

    while start < end:
        blending = juices[start] + juices[end]

        if min_blending > abs(blending):
            min_blending = abs(blending)
            ans_x, ans_y = start, end

        if blending < 0:
            start += 1
        else:
            end -= 1

    return ans_x, ans_y


ans_x, ans_y = search(0, n-1)
print(juices[ans_x], juices[ans_y])
