X, K, D = map(int, input().split())

ans = X
m = min(K, abs(X) // D) * D
if X < 0:
    ans += m
else:
    ans -= m
K -= abs(X) // D
if K > 0:
    if K % 2 == 1:
        if ans < 0:
            ans += D
        else:
            ans -= D

print(abs(ans))