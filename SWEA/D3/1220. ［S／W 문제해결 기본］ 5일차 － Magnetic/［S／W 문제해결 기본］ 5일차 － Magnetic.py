for t in range(1, 11):
    n = int(input())
    arr = []

    for i in range(n):
        arr.append(list(input().split()))

    answer = 0
    for i in range(n):
        tmp = ''
        for j in range(n):
            if arr[j][i] != '0':
                tmp += arr[j][i]
        answer += tmp.count('12')
    print(f'#{t} {answer}')
