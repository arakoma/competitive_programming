N = int(input())
R = [int(input()) for _ in range(N)]

R.sort(reverse=True)
s = 0
for i in range(N):#indexは0からです偶奇注意
    if i%2==0:
        s += R[i] ** 2
    else:
        s -= R[i] ** 2

import math
print(s * math.pi)

#########################
N = int(input())
R = [int(input()) for _ in range(N)]
# 一応こんな書き方もある
f = True # f = 0 でも良い
for i in range(N):
    if f:
        s += R[i] ** 2
    else:
        s -= R[i] ** 2
    f = not f

import math
print(s * math.pi)