N = int(input())
H = list(map(int, input().split()))

max_h = 0
for h in H:
    if h >= max_h:
        max_h = h
    else:
        if max_h - 1 == h:
            continue
        else:
            print("No")
            break
else:
    print("Yes")  