N, A, B = map(int, input().split())

x = N // (A + B)
y = N % (A + B)
ans = x * A + min(y, A)

print(ans)