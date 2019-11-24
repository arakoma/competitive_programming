N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

AB.sort(key=lambda x:(x[1],x[0]))
time = 0
for A, B in AB:
    time += A
    if B < time:
        print("No")
        break
else:
    print("Yes")
