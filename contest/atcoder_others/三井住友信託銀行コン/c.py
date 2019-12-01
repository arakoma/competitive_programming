X = int(input())

if X < 100:
    print(0)
else:
    y = X - X // 100 * 100

    if y // (X // 100) < 5:
        print(1)
    elif y // (X // 100) == 5 and y % (X // 100) == 0:
        print(1)
    else:
        print(0)