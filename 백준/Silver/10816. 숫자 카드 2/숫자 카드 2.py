from sys import stdin
from collections import Counter

n = int(stdin.readline())
counter = Counter(map(int, stdin.readline().split()))
m = int(stdin.readline())
numbers = list(map(int, stdin.readline().split()))
print(*[0 if (cnt := counter.get(number)) is None else cnt for number in numbers])
