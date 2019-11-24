W, a, b = map(int, input().split())
if a > b+W or b > a+W:
    print(min(abs(a+W-b), abs(b+W-a)))
else:
    print(0)