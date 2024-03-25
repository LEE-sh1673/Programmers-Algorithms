from sys import stdin

for _ in range(int(stdin.readline())):
    line = stdin.readline().strip()
    print(line[0], line[-1], sep='')
