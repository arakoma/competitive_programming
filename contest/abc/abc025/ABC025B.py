N, A, B = map(int, input().split())
sd = [list(input().split()) for _ in range(N)]
for i in range(N):
    sd[i][1] = int(sd[i][1])

ans = 0
for s,d in sd:
    if d < A:
        move = A
    elif A <= d <= B:
        move = d
    elif d > B:
        move = B

    if s == "West":
        ans -= move
    elif s == "East":
        ans += move

if ans < 0:
    print("West", -ans)
elif ans == 0:
    print(0)
elif ans > 0:
    print("East", ans)