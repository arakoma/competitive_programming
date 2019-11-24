import math

a, b, x = map(int, input().split())

if x <= b * a**2 / 2:
    theta = math.degrees(math.atan2(b, 2*x/a/b))
else:
    theta = math.degrees(math.atan2(2*(a*b-x/a)/a, a))

print(theta)