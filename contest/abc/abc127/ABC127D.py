N, M = map(int,input().split())
A = [[1,int(a)] for a in input().split()]
BC = A + [list(map(int,input().split())) for _ in range(M)]

BC.sort(key=lambda x:x[1], reverse=True)

i = 0
ans = 0
for B,C in BC:
    if i + B <= N:
        ans += B*C
        i += B
    else:
        ans += (N - i) * C
        break

print(ans)