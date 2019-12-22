N = int(input())

ans = 0
if N % 2 == 0:
    i = 0
    while True:
        x = (2 * 5 * (5 ** i))
        if x > N:
            break
        ans += N // x
        i += 1

print(ans)