X = int(input())

ans = X
for i in range(X+1):
    if i * (i + 1) // 2 >= X:
        ans = i
        break

print(ans)