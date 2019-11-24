N=int(input())
L = []
for i in range(1,N+1):
    S,P = input().split()
    if P == "0":
        L.append([i,S+"9999999999"])
    elif 100-int(P) < 10:
        L.append([i,S+"0"+str(100-int(P))])
    else:
        L.append([i,S+str(100-int(P))])

L.sort(key=lambda x:x[1])
for i in range(N):
    print(L[i][0])