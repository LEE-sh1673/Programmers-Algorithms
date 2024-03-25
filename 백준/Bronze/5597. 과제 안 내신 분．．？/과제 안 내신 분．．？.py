from sys import stdin

numbers = set(map(lambda x: int(x.strip()), stdin.readlines()))
numbers = set(range(1, 31)).difference(numbers)
print('\n'.join(map(str, sorted(numbers))))
