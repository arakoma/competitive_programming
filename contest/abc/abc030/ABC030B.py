n, m = map(int, input().split())

l = m * 6
if n >= 12:
    n -= 12
s = m * 0.5  + n * 30

d = abs(l-s)
if d <= 180:
    print(d)
else:
    print(360-d)