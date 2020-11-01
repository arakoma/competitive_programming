S = input()
ans = "No"

N = len(S)

if N >= 3:
    S = list(map(int, list(S)))
    cnt = [0 for _ in range(10)]
    for i in range(N):
        cnt[S[i]] += 1
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                flag = False
                c = cnt.copy()
                for x in [i, j, k]:
                    c[x] -= 1
                    if c[x] < 0:
                        flag = True
                if flag:
                    continue
                if (i*100+j*10+k) % 8 == 0:
                    ans = "Yes"
elif N == 2:
    if int(S) % 8 == 0 or int(S[::-1]) % 8 == 0:
        ans = "Yes"
elif N == 1:
    if int(S) % 8 == 0:
        ans = "Yes"

print(ans)
