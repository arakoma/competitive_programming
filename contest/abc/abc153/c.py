N, K = map(int, input().split())
H = list(map(int, input().split()))

H = sorted(H)[::-1]

cnt = 0
for i in range(N):
    if K > 0:
        K -= 1
    else:
        cnt += H[i]

print(cnt)