"""
A, B, C, X, Y = map(int, input().split())

ans = 5000 * 2 * 10 ** 5
for i in range(10 ** 5 + 1):
    s = i * 2 * C + max(0, X - i) * A + max(0, Y - i) * B
    ans = min(ans, s)

print(ans)
"""

A, B, C, X, Y = map(int, input().split())

if X > Y:
    v = A
else:
    v = B

ans = min(A*X+B*Y, C*max(X, Y)*2, C*min(X,Y)*2+(max(X,Y)-min(X,Y))*v)

print(ans)