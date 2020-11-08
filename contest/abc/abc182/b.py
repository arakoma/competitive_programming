N = int(input())
A = list(map(int, input().split()))

ans = 0
cnt = 0
for i in range(2, 1001):
    c = 0
    for a in A:
        if a % i == 0:
            c += 1
    if cnt < c:
        ans = i
        cnt = c

print(ans)