N = int(input())
A = list(map(int, input().split()))

L = [0 for _ in range(10 ** 5 + 2)]

for a in A:
    L[a] += 1

ans = 0
for i in range(1,100001):
    ans = max(ans,L[i-1]+L[i]+L[i+1])

print(ans)