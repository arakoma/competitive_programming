X = int(input())

ans = 0
money = 100
for i in range(1, 10**18):
    money = (money * 101) // 100
    if money >= X:
        ans = i
        break

print(ans)