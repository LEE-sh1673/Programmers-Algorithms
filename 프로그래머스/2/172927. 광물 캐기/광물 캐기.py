"""
[조건]
- 각 곡괭이는 종류에 상관없이 광물 5개를 캔 후에는 더 이상 사용할 수 없습니다.
- 사용할 수 있는 곡괭이 중 아무거나 하나를 선택해 광물을 캡니다.
- 한 번 사용하기 시작한 곡괭이는 사용할 수 없을 때까지 사용합니다.
- 광물은 주어진 순서대로만 캘 수 있습니다.
- 광산에 있는 모든 광물을 캐거나, 더 사용할 곡괭이가 없을 때까지 광물을 캡니다.

마인이 작업을 끝내기까지 필요한 최소한의 피로도를 계산

e.g.
dia:1, iron:3, stone:2 / 다이아3-철2-다이아1-철1-돌1

1. 다이아3-철2개를 다이아곡괭이로 캠 (1*3 + 1*2=5)
2. 다이아1개를 철곡괭이로 캠 (5*1 = 5)
3. 철1-돌1개를 철곡괭이로 캠 (1*1 + 1*1 = 2)
------------------------------------
피로도: 12

e.g.
dia:0 iron:1 stone:1 / 다이아5-철5-다이아1

1. 다이아5개를 철 곡괭이로 캠 (5*5=25)
2. 철5개를 돌 곡괭이로 캠 (5*5=25)
------------------------------------
피로도: 50

[풀이]
- 아래 과정을 모든 광물을 캘 때까지 반복한다.
    1. 순서대로 광물 5개를 뽑는다. -> (e.g. "diamond", "diamond", "diamond", "iron", "iron")
    2. 비용을 계산한다.
        - 다이아몬드 곡괭이 => (1*1 + 1*1 + ... + 1*1 = 5)
        - 철 곡괭이 => (5*1 + 5*1 + ... + 1*1 = 17)
        - 돌 곡괭이 => ...
    3. 최소 비용이 소모되는 곡괭이를 선택한다.
    4. 소모된 비용을 누적한다.
- 총 소모된 비용을 반환한다. (5 + 7 = 12)
"""
pick_mapper = [
    { "diamond": 1, "iron": 1, "stone":1 },
    { "diamond": 5, "iron": 1, "stone":1 },
    { "diamond": 25, "iron": 5, "stone":1 },
]


def pick_cost(pick_type, minerals):
    return sum([pick_mapper[pick_type][minaral] for minaral in minerals])


def solution(picks, minerals):
    answer = 0
    dia_picks, iron_picks, stone_picks = picks
    
    minerals = [minerals[i:i+5] for i in range(0, len(minerals), 5)][:sum(picks)]
    minerals = sorted(
        minerals,
        key=lambda x: (
            x.count("diamond"), 
            x.count("iron"), 
            x.count("stone")
        ),
        reverse=True
    )
    
    for mineral_subset in minerals:
        if dia_picks > 0:
            answer += pick_cost(0, mineral_subset)
            dia_picks -= 1
        elif iron_picks > 0:
            answer += pick_cost(1, mineral_subset)
            iron_picks -= 1
        elif stone_picks > 0:
            answer += pick_cost(2, mineral_subset)
            stone_picks -= 1

    return answer
