N = int(input())
ans = 0
for i in range(1, 10**9):
    if N < i ** 2:
        ans = (i-1) ** 2
        break
print(ans)