N = int(input())
D = list(map(int, input().split()))

D.sort()
if D[int(N/2)] == D[int(N/2-1)]:
    ans = 0
else:
    ans = D[int(N/2)] - D[int(N/2-1)]

print(ans)