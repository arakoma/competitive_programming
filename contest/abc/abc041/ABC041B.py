A, B, C = map(int, input().split())
print((A%(10**9+7) * B%(10**9+7) * C%(10**9+7)) % (10**9+7))