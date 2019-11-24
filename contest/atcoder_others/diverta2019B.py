R,G,B,N = map(int, input().split())

ans = 0
L = sorted([R,G,B], reverse=True)
for i in range(N//L[0]+1):
    for j in range((N-i*L[0])//L[1]+1):
        if (N-i*L[0]-j*L[1])%L[2] == 0:
                ans += 1

print(ans)