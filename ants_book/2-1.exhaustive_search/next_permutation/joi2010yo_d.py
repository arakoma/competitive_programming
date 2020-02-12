import itertools


n = int(input())
k = int(input())
c = [int(input()) for _ in range(n)]

L = []
for x in itertools.permutations(c, k):
    L.append("".join(map(str, x)))

ans = len(set(L))
print(ans)