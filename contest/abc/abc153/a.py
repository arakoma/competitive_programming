H, A = map(int, input().split())

if H / A == H // A:
    print(H // A)
else:
    print(H // A + 1)