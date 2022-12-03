import sys

lines = sys.stdin.readlines()
psum = 0
idx = 0
while idx + 2 < len(lines):
    e1 = set(item for item in lines[idx + 0].strip())
    e2 = set(item for item in lines[idx + 1].strip())
    e3 = set(item for item in lines[idx + 2].strip())
    d = e1.intersection(e2).intersection(e3).pop()
    v = ord(d) - 96 if d.islower() else ord(d) - 64 + 26
    psum += v
    idx += 3
print(psum)
