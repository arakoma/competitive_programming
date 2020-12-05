N = int(input())
s = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
c = [0 for _ in range(len(s))]
ans = 1
for i in range(1, N+1):
    n = i
    cn = [0 for _ in range(len(s))]
    for j in range(len(s)):
        while True:
            if n % s[j] == 0:
                cn[j] += 1
                n //= s[j]
            else:
                break
    for j in range(len(s)):
        c[j] = max(c[j], cn[j])

for i in range(len(s)):
    ans *= s[i] ** c[i]

ans += 1
print(ans)