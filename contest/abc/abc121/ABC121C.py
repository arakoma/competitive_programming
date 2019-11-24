n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

a =[]
for i in range(n):
    a.append(ab[i][0])

b = []
for i in range(n):
    b.append(ab[i][1])

x = 0 #本数
y = 0 #金額

while m > x:
    if b[a.index(min(a))] > 0:
        y += min(a)
        b[a.index(min(a))] -= 1
        x += 1
    else:
        del b[a.index(min(a))]
        del a[a.index(min(a))]
        continue

print(y)
#TLE

#######################################
#after_contest

n, m = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(n)]

ab.sort(key=lambda x:x[0])

cnt = 0
price = 0
i = 0
while cnt < m:
    price += ab[i][0] * ab[i][1]
    cnt += ab[i][1]
    if cnt > m:
        price -= ab[i][0] * (cnt - m)
        break
    i += 1

print(price)