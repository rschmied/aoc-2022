import sys

# A Rock      X   1  lose
# B Paper     Y   2  draw
# C Scissors  Z   3  win

results = {
    "A": {
        "X": 3 + 0,
        "Y": 1 + 3,
        "Z": 2 + 6,
    },
    "B": {
        "X": 1 + 0,
        "Y": 2 + 3,
        "Z": 3 + 6,
    },
    "C": {
        "X": 2 + 0,
        "Y": 3 + 3,
        "Z": 1 + 6,
    },
}

score = 0
for line in sys.stdin.readlines():
    a, b = line.strip().split()
    score += results[a][b]
print(score)
