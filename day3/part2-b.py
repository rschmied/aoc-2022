import sys

lines = iter(sys.stdin.readlines())
psum = 0
el = lambda l: set(item for item in l.strip())

while True:
    try:
        e1 = el(next(lines))
        e2 = el(next(lines))
        e3 = el(next(lines))
    except StopIteration:
        break
    d = e1.intersection(e2).intersection(e3).pop()
    psum += ord(d) - 96 if d.islower() else ord(d) - 64 + 26
print(psum)
