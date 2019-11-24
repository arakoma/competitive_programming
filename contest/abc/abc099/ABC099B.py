a, b = map(int, input().split())
ans = 0
for i in range(b-a):
    ans += i
print(ans - a)