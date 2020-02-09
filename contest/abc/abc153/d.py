H = int(input())

cnt = 1
ans = 1

if H == 1:
    ans = 1
else:
    while True:
        if H // 2 > 1:
            H //= 2
            ans += 2 ** cnt
            cnt += 1
        else:
            ans += 2 ** cnt
            break

print(ans)
