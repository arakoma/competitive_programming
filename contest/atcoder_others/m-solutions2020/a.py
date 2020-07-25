X = int(input())

ans = 0
if 400 <= X <= 599:
    ans = 8
elif 600 <= X <= 799:
    ans = 7
elif 800 <= X <= 999:
    ans = 6
elif 1000 <= X <= 1199:
    ans = 5
elif 1200 <= X <= 1399:
    ans = 4
elif 1400 <= X <= 1599:
    ans = 3
elif 1600 <= X <= 1799:
    ans = 2
elif 1800 <= X <= 1999:
    ans = 1

print(ans)