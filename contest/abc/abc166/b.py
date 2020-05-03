N, K = map(int, input().split())
sunuke = [1] * N

for _ in range(K):
    d = int(input())
    A = list(map(int, input().split()))
    for a in A:
        sunuke[a-1] = 0
    
ans = sum(sunuke)
print(ans)