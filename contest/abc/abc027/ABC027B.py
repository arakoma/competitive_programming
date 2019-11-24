N = int(input())
a = list(map(int, input().split()))

if sum(a) % N != 0:
    print(-1)
else:
    cnt = 0
    for i in range(1,N):
        if sum(a[:i])/i != sum(a[i:])/(N-i):
            cnt += 1
    print(cnt)