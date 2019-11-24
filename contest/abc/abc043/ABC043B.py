s = list(input())

ans = ""
for x in s:
    if x == 'B':
        if len(ans) != 0:
            ans = ans[:-1]
    else:
        ans += x

print(ans)