import sys

# A Rock      X   1  lose
# B Paper     Y   2  draw
# C Scissors  Z   3  win

results = {
    "A": {
        "X": 1 + 3,
        "Y": 2 + 6,
        "Z": 3 + 0,
    },
    "B": {
        "X": 1 + 0,
        "Y": 2 + 3,
        "Z": 3 + 6,
    },
    "C": {
        "X": 1 + 6,
        "Y": 2 + 0,
        "Z": 3 + 3,
    },
}

score = 0
for line in sys.stdin.readlines():
    a, b = line.strip().split()
    score += results[a][b]
print(score)
