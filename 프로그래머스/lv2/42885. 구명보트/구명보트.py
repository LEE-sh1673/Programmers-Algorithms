from collections import deque


def solution(people, limit):
    q = deque()

    for person in sorted(people):
        q.append(person)

    nums_pair = 0
    
    while q:
        big = q.pop()

        if not q:
            break

        small = q[0]

        if small + big <= limit:
            q.popleft()
            nums_pair += 1

    return len(people) - nums_pair
