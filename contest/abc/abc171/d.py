N = int(input())
A = list(map(int, input().split()))
Q = int(input())
BC = [list(map(int, input().split())) for _ in range(Q)]

s = 0
cnt = [0] * (10**5+1)
for a in A:
    cnt[a] += 1
    s += a

for b, c in BC:
    n = cnt[b]
    s -= b * n
    s += c * n
    cnt[c] += n
    cnt[b] = 0
    print(s)
