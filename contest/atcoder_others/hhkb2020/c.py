N = int(input())
P = list(map(int, input().split()))

exist = [0 for _ in range(2*(10**5)+5)]
min_now = 0
ans = []

for p in P:
    exist[p] = 1
    if p == min_now:
        for i in range(p, 2*(10**5)+4):
            if exist[i] == 0:
                min_now = i
                break
    ans.append(min_now)

for a in ans:
    print(a)