X, Y = map(int, input().split())

ans = "No"
for i in range(101):
    for j in range(101):
        if i + j == X and i * 2 + j * 4 == Y:
            ans = "Yes"

print(ans)