"""
LV2. 거리두기 확인하기
[https://school.programmers.co.kr/learn/courses/30/lessons/81302]

조건:
- 대기실은 5개이며, 각 대기실은 5x5
- 응시자들 끼리는 맨해튼 거리 > 2 유지
    - 단 응시자가 앉아있는 자리 사이가 파티션으로 막혀 있을 경우에는 허용
- 거리두기를 지키고 있으면 1을, 한 명이라도 지키지 않고 있으면 0
    - P는 응시자가 앉아있는 자리를 의미합니다.
    - O는 빈 테이블을 의미합니다.
    - X는 파티션을 의미합니다.
"""


def solution(places):
    answer = []

    for place in places:
        is_valid = True

        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P' and not check(i, j, place):
                    is_valid = False
                    break

            if not is_valid:
                break

        answer.append(1 if is_valid else 0)
    return answer


def check(i, j, place):
    """
    bfs로 거리두기 준수 여부 탐색
    """
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    que = [(i, j, 0)]

    while que:
        x, y, dist = que.pop(0)

        for dir_x, dir_y in dirs:
            pos_x, pos_y = x + dir_x, y + dir_y

            if pos_x < 0 or pos_x > 4 or pos_y < 0 or pos_y > 4:
                continue

            if i == pos_x and j == pos_y:
                continue

            if place[pos_x][pos_y] == 'P':
                return False

            if place[pos_x][pos_y] == 'O' and dist + 1 < 2:
                que.append([pos_x, pos_y, dist + 1])
    return True
