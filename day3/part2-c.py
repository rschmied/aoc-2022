import sys

lines = iter(sys.stdin.readlines())
psum = 0
el = lambda l: set(item for item in l.strip())

for line in lines:
    e1 = el(line)
    e2 = el(next(lines))
    e3 = el(next(lines))
    d = e1.intersection(e2).intersection(e3).pop()
    psum += ord(d) - 96 if d.islower() else ord(d) - 64 + 26
print(psum)
