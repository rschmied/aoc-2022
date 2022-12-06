import sys

MLEN = 4
# MLEN = 14
idx = 0
data = sys.stdin.readline().strip()
for idx in range(len(data) - MLEN + 1):
    if len(set(data[idx : idx + MLEN])) == MLEN:
        break
print(idx + MLEN)
