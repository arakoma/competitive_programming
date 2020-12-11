N = int(input())
MTmT = [list(map(float, input().split())) for _ in range(N)]

ans = [0 for _ in range(6)]

for MT, mT in MTmT:
    if MT >= 35:
        ans[0] += 1
    elif 30 <= MT < 35:
        ans[1] += 1
    elif 25 <= MT < 30:
        ans[2] += 1
    
    if mT >= 25:
        ans[3] += 1
    elif mT < 0 and MT >= 0:
        ans[4] += 1
    elif MT < 0:
        ans[5] += 1

print(" ".join(map(str, ans)))