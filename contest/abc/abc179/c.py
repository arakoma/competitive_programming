N = int(input())

ans = 0

for a in range(1, N+1):
    if N % a == 0:
        ans += N // a - 1
    else:
        ans += N // a

print(ans)