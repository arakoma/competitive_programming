N, X = map(int, input().split())
L = list(map(int, input().split()))

cnt = 1
tmp = 0
for i in L:
    tmp += i
    if tmp <= X:
        cnt += 1

print(cnt)