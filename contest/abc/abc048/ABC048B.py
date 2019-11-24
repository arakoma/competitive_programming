a, b, x = map(int, input().split())
if a != 0:
    print(b//x - (a-1)//x)
elif a == 0:
    print(b//x + 1) # 0もxで割り切れる