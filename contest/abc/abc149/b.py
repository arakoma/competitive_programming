A, B, K = map(int, input().split())

a = 0
b = 0

a = max(a, A - K)
K = max(0, K - A)
b = max(b, B - K)

print(str(a) + " " + str(b))