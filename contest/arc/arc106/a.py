N = int(input())
ans = -1
for a in range(1, 1000):
    for b in range(1, 1000):
        if 3 ** a + 5 ** b == N:
            ans = [a, b]
            break

if ans == -1:
    print(ans)
else:
    print(" ".join(map(str, ans)))