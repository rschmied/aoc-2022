import re
import sys
from typing import Dict, Iterator, List, Tuple

re1 = r"^\$ (ls|cd)( .*)?$"


def process(
    lines: Iterator[str], dirs: Dict[str, List[Tuple[int, str]]], dir: str = ""
):
    cwd = dir
    while True:
        try:
            line = next(lines)
        except StopIteration:
            return
        if m := re.match(re1, line):
            cmd = m.group(1)
            arg = None if m.group(2) is None else m.group(2).strip()
            match cmd:
                case "cd":
                    if arg == "..":
                        return
                    cwd = f"{arg}" if dir == "" else f"{dir}{arg}/"
                    dirs[cwd] = []
                    continue
                case "ls":
                    process(lines, dirs, cwd)
                    continue
                case _:
                    raise
        part1, part2 = line.strip().split()
        if part1 == "dir":
            dirs[dir].append((-1, part2))
            continue
        dirs[dir].append((int(part1), part2))


def dir_sum(dirs: Dict[str, List[Tuple[int, str]]], dir: str) -> int:
    sum = 0
    for size, name in dirs[dir]:
        if size < 0:  # dir?
            sum += dir_sum(dirs, f"{dir}{name}/")
        else:
            sum += size
    return sum


if __name__ == "__main__":
    lines = iter(sys.stdin.readlines())
    dirs: Dict[str, List[Tuple[int, str]]] = {}
    process(lines, dirs)

    # part 1
    total_sum = 0
    for k in dirs.keys():
        dsum = dir_sum(dirs, k)
        print(k, dsum)
        if dsum <= 100_000:
            total_sum += dsum
    print("\nSum of directories smaller than 100k:", total_sum)

    # part 2
    total = 70_000_000
    used = dir_sum(dirs, "/")
    free = total - used
    print("Total free space:", free)
    needed: int = 30_000_000
    current: int = total
    dir_to_delete = "unknown"

    for k in dirs.keys():
        dsum = dir_sum(dirs, k)
        if free + dsum >= needed and dsum < current:
            current = dsum
            dir_to_delete = k
    print("Directory to remove:", dir_to_delete)
    space = dir_sum(dirs, dir_to_delete)
    print("Freed up space:", space)
    print("Resulting freespace:", free + space)
