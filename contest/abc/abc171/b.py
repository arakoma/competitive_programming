N, K = map(int, input().split())
p = list(map(int, input().split()))

p = sorted(p)
ans = sum(p[:K])
print(ans)
