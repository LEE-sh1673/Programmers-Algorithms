"""
9081. 단어 맞추기

패턴1: 자릿수 2자리의 순서가 바뀌는 경우
- e.g. BEER -> BERE (1223 -> 1232)

패턴2: 맨 앞의 자릿수가 바뀌고, 그 뒤의 자릿수가 오름차순 정렬
- e.g. BREE -> EBER (1322 -> 2123)

정리하자면 다음 순서가 맨 오른쪽부터 왼쪽 방향으로 재귀적으로 발생되는 패턴이다.

1. i= N-2부터 시작하여, 아래를 반복:
    num[i], num[i+1]에 대해
    1-A. num[i] < num[i+1] 이라면,
        1. num[i+1] ~ num[N] 사이에 num[i] < num[k]에 만족하면서 최솟값을 가진 k를 찾는다.
        2. num[i]와 num[k]를 교환한다.
        3. num[i+1] 부터 num[N]까지 오름차 순으로 정렬한다.
    1-B. num[i] >= num[i+1]이면 패스한다.
    2. 자릿수를 왼쪽으로 1증가 i = (i - 1) % N
2. 현재 자릿수가 처음 자릿수를 뒤집었을 때와 동일하거나, 1-A에서 <1>에 만족하는 k가 없는 경우 탐색을 종료한다.

BEER -> 1223
BERE -> 1232
BREE -> 1322
EBER -> 2123
EBRE -> 2132
EEBR -> 2213
EERB -> 2231
ERBE -> 2312
EREB -> 2321
RBEE -> 3122
REBE -> 3212
REEB -> 3221
"""
for _ in range(int(input().strip())):
    word = input()
    N = len(word)
        
    if N == 2:
        print(word[::-1])
        continue

    start = list(word)
    prev, answer = "".join(start), ""

    while True:
        i = N - 1
        
        while i != 0 and start[i - 1] >= start[i]:
            i = (i - 1) % N

        if i == 0:
            answer = prev
            break

        """
        1-A. num[i-1] < num[i] 이라면,
            1. num[i] ~ num[N] 사이에 num[i-1] < num[k]에 만족하면서 최솟값을 가진 k를 찾는다.
            2. num[i-1]와 num[k]를 교환한다.
            3. num[i] 부터 num[N]까지 오름차 순으로 정렬한다.
        """
        min_k = max(k for k in range(i, N) if start[k] > start[i - 1])
        start[i - 1], start[min_k] = start[min_k], start[i - 1]
        start = start[:i] + sorted(start[i:N])

        if prev == word:
            answer = "".join(start)
            break

        prev = "".join(start)

    print(answer)
