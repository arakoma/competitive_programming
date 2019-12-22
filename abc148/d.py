N = int(input())
a = list(map(int, input().split()))

cnt = 1
destroy = 0
for i in range(N):
    if a[i] == cnt:
        cnt += 1
    else:
        destroy += 1

if cnt == 1:
    print(-1)
else:
    print(destroy)