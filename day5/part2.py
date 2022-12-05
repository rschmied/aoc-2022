import sys

data = [line for line in sys.stdin.readlines()]
mark = data.index("\n")
commands = [
    (int(e[1]), int(e[3]), int(e[5])) for e in [l.split() for l in data[mark + 1 :]]
]
cols = int(data[mark - 1].split()[-1])

rawstacks = data[: mark - 1]
rawstacks.reverse()

stacks = [[] for _ in range(cols)]
for row in rawstacks:
    for col in range(cols):
        crate = row[col * 4 + 1]
        if crate != " ":
            stacks[col].append(crate)

for cmd in commands:
    move_count, from_stack, to_stack = cmd
    # this makes part2:
    crates = stacks[from_stack - 1][-move_count:]
    stacks[from_stack - 1] = stacks[from_stack - 1][:-move_count]
    stacks[to_stack - 1].extend(crates)

for col in range(cols):
    print(stacks[col][-1], end="")
print()
