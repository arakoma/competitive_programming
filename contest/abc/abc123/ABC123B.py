a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
li = [a,b,c,d,e]

for i in range(len(li)):
    if li[i]%10 != 0:
        if li[i]%10 == min([x%10 if x%10 != 0 else 10 for x in li]):
            N = i+0
            break
else:
    N = 0


for j in range(len(li)):
    if j == N:
        continue
    elif li[j]%10 != 0:
        li[j] += 10 - li[j]%10

print(sum(li))

######################
#全部1の位を10に上げてから
#１の位が0以外で一番小さいものについてを最後に引けばいい

a = [int(input()) for _ in range(5)]

m = 0#1の位が0以外で一番小さいもの(10との差が一番大きいもの)
sum_a = 0#10倍数にしたものの合計
for x in a:
    if x%10 != 0:
        t = 10 - x%10#10倍数との差
    else:
        t = 0
    sum_a += x+t
    m = max(m, t)

print(sum_a - m)#1の位が10から一番遠いもの(0除く)の差のみを最後に引く