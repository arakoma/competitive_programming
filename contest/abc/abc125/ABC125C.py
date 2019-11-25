N = int(input())
A = list(map(int, input().split()))

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

L = [0] * (N+1)
R = [0] * (N+1)
for i in range(1, N+1):
    L[i] = gcd(L[i-1], A[i-1])
for i in range(N)[::-1]:
    R[i] = gcd(R[i+1], A[i])

M = [gcd(L[i], R[i+1]) for i in range(N)]

print(max(M))