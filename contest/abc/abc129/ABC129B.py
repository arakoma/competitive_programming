n = int(input())
w = list(map(int,input().split()))

ans = 100*100
for i in range(1, n):
    x = abs(sum(w[:i]) - sum(w[i:]))
    ans = min(ans, x)

print(ans)