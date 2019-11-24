N = int(input())
SP = [list(input().split()) for _ in range(N)]

P_sum = 0
for i in range(N):
    P_sum += int(SP[i][1])

for s, p in SP:
    if int(p) > P_sum/2:
        print(s)
        break
else:
    print("atcoder")
    
###############
N=int(input())
S=[]
P=[]
for _ in range(N):
  s, p = input().split()
  S.append(s)
  P.append(int(p))
K=sum(P)
ans='atcoder'
for i in range(N):
  if K < P[i]*2:
    ans = S[i]
print(ans)
