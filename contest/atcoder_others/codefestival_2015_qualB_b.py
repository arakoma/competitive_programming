N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

ans = -1
cnt = 0

for a in A:
    if a == ans:
        cnt += 1
    else:
        if cnt > N // 2:
            break
        ans = a
        cnt = 1
else:
    if cnt <= N // 2:
        ans = "?"

print(ans)
