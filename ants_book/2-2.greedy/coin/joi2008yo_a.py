n = int(input())
x = 1000 - n

ans = 0
while True:
    if x >= 500:
        x -= 500
        ans += 1
    elif 100 <= x < 500:
        x -= 100
        ans += 1
    elif 50 <= x < 100:
        x -= 50
        ans += 1
    elif 10 <= x < 50:
        x -= 10
        ans += 1
    elif 5 <= x < 10:
        x -= 5
        ans += 1
    elif 0 < x < 5:
        ans += x
        x = 0
    if x == 0:
        break

print(ans)
