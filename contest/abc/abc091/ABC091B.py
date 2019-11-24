n = int(input())
s = [input() for _ in range(n)]
m = int(input())
t = [input() for _ in range(m)]

ans = 0
for i in s:
    yen = s.count(i) - t.count(i)
    if ans <= yen:
        ans = yen

print(ans)