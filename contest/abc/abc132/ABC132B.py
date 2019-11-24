N = int(input())
P = list(map(int,input().split()))

cnt = 0
for i in range(1,N-1):
    ppp = [P[i-1], P[i], P[i+1]]
    ppp.sort()
    if ppp[1] == P[i] and ppp[1] != ppp[0]:
        cnt += 1

print(cnt)