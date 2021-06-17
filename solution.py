import sys
input = sys.stdin.readline

h, w = map(int, input().split())
blocks = list(map(int, input().split()))
water = 0

for j in range(h):
    i, first, last = 0, -1, -1
    while i < w:
        if first == -1 and blocks[i] > j:
            first = i
        if last == -1 and blocks[(i*-1) -1] > j:
            last = w -i -1
        i += 1

    if first != last:
        for idx, val in enumerate(blocks):
            if val <= j:
                if idx > first and idx < last:
                    water += 1

print(water)
