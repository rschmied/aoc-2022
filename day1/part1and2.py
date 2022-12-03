import sys

elf = 0
elves = []

for line in sys.stdin.readlines():
    if line.strip():
        elf += int(line)
    else:
        elves.append(elf)
        elf = 0
elves.append(elf)

elves.sort(reverse=True)
print(elves[0], sum(elves[0:3]))
