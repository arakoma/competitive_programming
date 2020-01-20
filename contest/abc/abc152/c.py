N = int(input())
P = list(map(int, input().split()))

ans = 0
a = 2 * 10 ** 5 + 1
for i in range(N):
    if P[i] <= a:
        ans += 1
        a = P[i]

print(ans)