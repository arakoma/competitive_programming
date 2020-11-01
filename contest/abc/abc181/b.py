N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for a, b in AB:
    ans += b * (b + 1) // 2 - (a - 1) * a // 2

print(ans)