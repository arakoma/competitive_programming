def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


A, B = map(int, input().split())

ans = A * B // gcd(A, B)

print(ans)