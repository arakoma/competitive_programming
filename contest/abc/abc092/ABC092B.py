n = int(input())
d, x = map(int, input().split())
a = [int(input()) for _ in range(n)]

eat = 0
for i in range(n):
    for j in range(d):
        if a[i]*j+1 <= d:
            eat += 1
        else:
            break

print(eat + x)
##############################
#2重for回さなくても割ればよかったん
n = int(input())
d, x = map(int, input().split())
a = [int(input()) for _ in range(n)]

for A in a:
    x += (d-1)//A + 1
print(x)