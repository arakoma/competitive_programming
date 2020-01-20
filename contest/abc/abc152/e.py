def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a // gcd(a, b) * b


N = int(input())
A = list(map(int, input().split()))
mod = 10 ** 9 + 7

lcm_ = 1
for i in range(N):
    lcm_ = lcm(lcm_, A[i])

ans = 0
for i in range(N):
    ans += lcm_ // A[i]

print(ans % mod)