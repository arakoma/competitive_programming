N, Y = map(int, input().split())

flag = False
for x in range(N+1):
    for y in range(N-x+1):
        z = N - (x + y)
        if Y == 10000 * x + 5000 * y + 1000 * z:
            flag = True
            print(x, y, z)
            break
    if flag:
        break
else:
    print(-1, -1, -1)