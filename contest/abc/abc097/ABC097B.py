x = int(input())

ans = 1
for i in range(1, x):
    for j in range(2, x):
        if i**j <= x:
            ans = max(ans, i**j)
        else:
            break

print(ans)

#range()で第一引数>=第二引数の場合は空のlistを返す