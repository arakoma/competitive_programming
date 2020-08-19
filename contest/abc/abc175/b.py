N = int(input())
L = list(map(int, input().split()))

ans = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            t = [L[i], L[j], L[k]]
            t.sort()
            if len(set(t)) == 3 and (t[0] + t[1]) > t[2]:
                ans += 1

print(ans)
