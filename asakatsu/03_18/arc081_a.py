N = int(input())
A = list(map(int, input().split()))

A = sorted(A)[::-1]
a = []
ng = 9999999
for i in range(N-1):
    if i != ng:
        if A[i] == A[i+1]:
            a.append(A[i])
            ng = i+1
            if len(a) == 2:
                break

ans = 0
if len(a) == 2:
    ans = a[0] * a[1]
else:
    ans = 0

print(ans)
