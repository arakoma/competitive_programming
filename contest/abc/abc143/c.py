N = int(input())
S = list(input())

ans = 0
x = 'xxxxxxxx'
for s in S:
    if s != x:
        ans += 1
    x = s

print(ans)