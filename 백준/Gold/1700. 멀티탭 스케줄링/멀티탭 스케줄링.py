from collections import defaultdict
from sys import stdin

input = stdin.readline
n, k = map(int, input().split())
tasks = list(map(int, input().split()))
items = defaultdict(list)
plugs = []
replace_count = 0


def priority(name):
    return -(items[name][0] if items[name] else 101)


for idx, task in enumerate(tasks):
    items[task].append(idx)

for idx, task in enumerate(tasks):
    # 이미 플러그에 꽂혀 있는 경우
    if task in plugs:
        items[task].remove(idx)
        continue

    # 빈 곳이 존재하는 경우
    if len(plugs) < n:
        plugs.append(task)
        items[task].remove(idx)
    else:
        # 교체하는 경우
        replace_item = min(plugs, key=lambda name: priority(name))
        plugs.remove(replace_item)
        plugs.append(task)
        items[task].remove(idx)

        if not items[replace_item]:
            items.pop(replace_item)
        replace_count += 1

print(replace_count)
