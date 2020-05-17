import math


A, B, H, M = map(int, input().split())

m = M * 6
h = H * 30 + M * 0.5
s = min(abs(m-h), abs(h-m))

ans = (A ** 2 + B ** 2 - 2 * A * B * math.cos(math.radians(s))) ** 0.5

print(ans)