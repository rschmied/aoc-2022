import re
import sys

regex = r"^(\d+)-(\d+),(\d+)-(\d+)$"
part1_overlap = 0
part2_overlap = 0
for line in sys.stdin.readlines():
    if m := re.match(regex, line):
        r1 = list(range(int(m[1]), int(m[2]) + 1))
        r2 = list(range(int(m[3]), int(m[4]) + 1))
        if all([item in r1 for item in r2]) or all([item in r2 for item in r1]):
            part1_overlap += 1
        if any([item in r1 for item in r2]) or any([item in r2 for item in r1]):
            part2_overlap += 1
print(part1_overlap, part2_overlap)
