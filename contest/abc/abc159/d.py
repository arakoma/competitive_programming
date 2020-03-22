N = int(input())
A = list(map(int, input().split()))

cnt = 0
L = [0] * (N + 1)
for a in A:
    L[a] += 1

for l in L:
    cnt += l * (l - 1) // 2

for a in A:
    ans = cnt - (L[a] * (L[a] - 1) // 2) + ((L[a] - 1) * (L[a] - 2) // 2)
    print(ans)