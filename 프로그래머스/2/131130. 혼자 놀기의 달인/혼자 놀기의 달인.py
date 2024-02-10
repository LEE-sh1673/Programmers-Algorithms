"""
[1번 그룹]
1. 2부터 100 이하의 자연수를 정한다.
2. 해당 수만큼 상자를 준비하고, 그 상자들을 무작위로 섞어 나열한다.
3. 상자가 나열된 순서에 따라 순번을 붙인다.
4. 임의로 상자를 선택한다.
5. 상자 안에 적힌 숫자에 해당하는 번호를 가진 상자를 선택한다.
6. 이 과정을 열어야 하는 상자가 이미 열려있을 때까지 반복한다.

[2번 그룹]
- 1번 그룹 상자 그룹과 다른 상자들이 섞이지 않도록 따로 둔다.
    - 이때 1번 상자 그룹을 제외하고 남는 상자가 없다면 0점이 된다.
    - 1번 그룹에 포함되지 않은 상자 하나를 골라 이미 열러 있는 상자를 만날 때까지 계속 진행한다.
    - 이때 최종 점수는 (1번 그룹 상자의 수) * (2번 그룹 상자의 수)
    
[8,6,3,7,2,5,1,4]
(1,8)
(2,6)
(3,3)
(4,7)
(5,2)
(6,5)
(7,1)
(8,4)

8 -> 4 -> 7 -> 1

"""
def group_counts(cards):
    visited = [False] * len(cards)
    
    def count_members(cards, start):
        nonlocal visited
        new_cards = []
        group_members = 0
    
        while not visited[start-1]:
            visited[start-1] = True
            start = cards[start-1]
            group_members += 1
        return group_members
    
    counts = []
    for idx, card in enumerate(cards):
        if not visited[idx]:
            counts.append(count_members(cards, cards[idx]))
    return sorted(counts, reverse=True)


def solution(cards):
    if len(counts := group_counts(cards)) > 1:
        return counts[0] * counts[1]
    return 0
