a, b, k = map(int, input().split())

ans = list(range(a, a+k)) + list(range(b-k+1, b+1))
ans.sort()
ans2 = []
for i in ans:
    if a<=i<=b and i not in ans2:
        ans2.append(i)

for j in ans2:
    print(j)
###########################
a, b, k = map(int, input().split())

li = range(a, b+1)
for i in sorted(set(li[:k]) | set(li[-k:])):
    print(i)