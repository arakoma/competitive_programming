D = int(input())#D=365
c = list(map(int, input().split()))#0<=c<=100
s = [list(map(int, input().split())) for _ in range(D)]#0<=s<=20000

t = [int(input()) for _ in range(D)]


v = []
last = [0] * 26
value = 0
for d in range(D):
    type = t[d]
    value += s[d][type - 1]
    last[type - 1] = d + 1
    for i in range(26):
        value -= c[i] * (d + 1 - last[i])
    v.append(value)

for i in range(D):
    print(v[i])
