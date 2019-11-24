n, x = map(int, input().split())
m = [int(input()) for _ in range(n)]

Xrest = x - sum(m)
ans = len(m)
while Xrest >= min(m):
    Xrest -= min(m)
    ans += 1

print(ans)

#######################
n, x = map(int, input().split())
m = [int(input()) for _ in range(n)]
print(n+(x-sum(m))//min(m))