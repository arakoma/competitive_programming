M, D = map(int, input().split())

cnt = 0
for m in range(1, M+1):
    for d in range(1, D+1):
        if d >= 10:
            d10 = int(str(d)[0])
            d1 = int(str(d)[1])
            if d10 >= 2 and d1 >= 2:
                if d10 * d1 == m:
                    cnt += 1

print(cnt)

###
N , K = map(int, input().split())
A = list(map(int, input().split()))

whole = 0
right = 0

for i in range(N):
    for j in range(N):
        if A[i] > A[j]:
            whole += 1
            if i < j:
                right += 1

mod = 10 ** 9 + 7
ans = right * K
ans += whole * (K - 1) * K // 2

print(ans % mod)