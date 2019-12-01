N = int(input())
S = list(map(int, list(input())))

cnt = 0

for i in range(10):
    for j in range(10):
        for k in range(10):
            pin = [i, j, k]
            x = 0

            for a in S:
                if a == pin[x]:
                    x += 1
                    if x == 3:
                        cnt += 1
                        break

print(cnt)

#pypyだと通った