N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

dicD = {}
dicT = {}

for d in D:
    if d not in dicD:
        dicD[d] = 0
    dicD[d] += 1

for t in T:
    if t not in dicT:
        dicT[t] = 0
    dicT[t] += 1

for t in dicT:
    if (t not in dicD) or (dicT[t] > dicD[t]):
        print("NO")
        break
else:
    print("YES")