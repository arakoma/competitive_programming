N = int(input())
ans = 100000
for i in range(1, 11):
    if i * 1000 - N >= 0:
        ans = i * 1000 - N
        break

print(ans)