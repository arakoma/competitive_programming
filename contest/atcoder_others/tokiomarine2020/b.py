A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())

ans = ""

if A < B:
    a = A + V * T
    b = B + W * T
    if a >= b:
        ans = "YES"
    else:
        ans = "NO"
else:
    a = A - V * T
    b = B - W * T
    if a <= b:
        ans = "YES"
    else:
        ans = "NO"

print(ans)
