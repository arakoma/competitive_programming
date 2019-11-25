###TLE
N = int(input())
s = [input() for _ in range(N)]

ss = []
cnt = 0
for i in range(N):
    x = "".join(sorted(list(s[i])))
    if x in ss:
        cnt += ss.count(x)
    ss.append(x)

print(cnt)


###AC
from collections import Counter

N = int(input())
S = [input() for _ in range(N)]

ctr = Counter()
ans = 0
for Si in S:
    x = "".join(sorted(list(Si)))
    if x in ctr:
        ans += ctr[x]
    ctr[x] += 1

print(ans)

###AC
N = int(input())
S = [input() for _ in range(N)]

cnt = {}
ans = 0

for Si in S:
    x = "".join(sorted(list(Si)))
    if x not in cnt:
        cnt[x] = 0
    ans += cnt[x]
    cnt[x] += 1

print(ans)