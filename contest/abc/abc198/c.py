r, x, y = map(int, input().split())
d = (x ** 2 + y ** 2) ** 0.5
if d == 0:
    ans = 0
elif d < r:
    ans = 2
elif d % r == 0:
    ans = d // r
else:
    ans = d // r + 1
print(int(ans))