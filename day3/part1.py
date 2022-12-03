import sys

sum = 0
for line in sys.stdin.readlines():
    items = line.strip()
    a, b = line[0 : len(items) // 2], line[len(items) // 2 :]
    d = set(item for item in a).intersection(set(item for item in b)).pop()
    v = ord(d) - 96 if d.islower() else ord(d) - 64 + 26
    sum += v
print(sum)
