def solution(n, computers):
    parents = [i for i in range(n)]

    def find(a):
        if parents[a] == a:
            return a
        
        parents[a] = find(parents[a])
        return parents[a]

    def union(a, b):
        a_p = find(a)
        b_p = find(b)

        if a_p < b_p:
            parents[b_p] = a_p
        else:
            parents[a_p] = b_p

    for row in range(n):
        for col in range(n):
            if row == col:
                continue

            if computers[row][col]:
                union(row, col)

    ans = set()

    for i in range(n):
        ans.add(find(parents[i]))
        
    return len(ans)