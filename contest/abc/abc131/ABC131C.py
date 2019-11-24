A, B, C, D = map(int, input().split())
A -= 1
def gcd(a, b):
	while b:
		a, b = b, a % b
	return a
def lcm(a, b):
	return a * b // gcd(a, b)

lcm = lcm(C, D)
# A
Ax = A // lcm
Ay = A // C
Az = A // D
AA = Ay + Az -Ax
a = A - AA
# B
Bx = B // lcm
By = B // C
Bz = B // D
BB = By + Bz -Bx
b = B - BB

print(b - a)