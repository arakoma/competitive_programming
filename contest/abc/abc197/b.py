h, w, x, y = map(int, input().split())
s = [input() for _ in range(h)]

ans = 1
x, y = x-1, y-1

if y != 0:
    for dy in range(0, y)[::-1]:
        if s[x][dy] == "#":
            break
        ans += 1
if y != w-1:
    for dy in range(y+1, w):
        if s[x][dy] == "#":
            break
        ans += 1

if x != 0:
    for dx in range(0, x)[::-1]:
        if s[dx][y] == "#":
            break
        ans += 1
if x != h-1:
    for dx in range(x+1, h):
        if s[dx][y] == "#":
            break
        ans += 1

print(ans)