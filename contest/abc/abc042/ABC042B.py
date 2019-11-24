N, L = map(int, input().split())
S = [input() for _ in range(N)]

S.sort()
ans = ""
for x in S:
    ans += x

print(ans)