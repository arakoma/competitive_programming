N = int(input())
s, t = input().split()

ans = ""
for i in range(N):
    ans += s[i]
    ans += t[i]

print(ans)