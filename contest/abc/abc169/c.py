from decimal import *

a, b = map(float, input().split())

a = Decimal(str(a))
b = Decimal(str(b))
b *= Decimal(str(100))
ans = a * b
ans //= Decimal(str(100))

print(ans)

"""
a, b = input().split()
a = int(a)
b = int(b.replace(".", ""))
ans = a * b // 100
print(ans)
"""