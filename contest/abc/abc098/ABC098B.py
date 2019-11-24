n = int(input())
sli = list(input())

ans = 0
for i in range(1, n-1):
    x = len(set(sli[:i]) & set(sli[i:]))
    if ans < x:
        ans = x

print(ans)