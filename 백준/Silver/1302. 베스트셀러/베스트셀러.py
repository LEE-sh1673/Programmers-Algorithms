n = int(input())
names = [input() for _ in range(n)]
name_hash = { name : 0 for name in names }

for name in names:
    name_hash[name] += 1

t = sorted(name_hash.items(), key=lambda x : (-x[1], x[0]))
print(t[0][0])
