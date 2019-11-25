S = input()
T = input()

cnt = 0
for i in range(3):
    if S[i] == T[i]:
        cnt += 1

print(cnt)

###
A, B = map(int, input().split())

if B == 1:
    ans = 0
elif A >= B:
    ans = 1
else:
    if (B - 1) % (A - 1) > 0:
        ans = (B - 1) // (A - 1) + 1
    else:
        ans = (B - 1) // (A - 1)

print(ans)

###
N = int(input())
H = list(map(int, input().split()))

cnt = 0
ans = 0
for i in range(N-1):
    if H[i+1] <= H[i]:
        cnt += 1
    else:
        if ans < cnt:
            ans = cnt + 0
        cnt = 0
else:
    if ans < cnt:
        ans = cnt + 0

print(ans)

###
N = int(input())

if N == 1:
    ans = 0
else:
    ans = N * (N + 1) // 2 - N

print(ans)

###
