S = [input() for _ in range(12)]
ans = 0
for x in S:
    if 'r' in x:
        ans += 1
print(ans)

###############
S = [input() for _ in range(12)]

ans = 0
for x in S:
    for i in range(len(x)):
        if x[i] == 'r':
            ans += 1
            break
print(ans)