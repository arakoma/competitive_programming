def gcd(a, b):
	while b:
		a, b = b, a % b
	return a


K = int(input())

ans = 0

for a in range(1, K+1):
    for b in range(1, K+1):
        d = gcd(a, b)
        for c in range(1, K+1):
            ans += gcd(d, c)

print(ans)