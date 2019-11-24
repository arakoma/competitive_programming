L, H = map(int, input().split())
N = int(input())
A = [int(input()) for _ in range(N)]

for a in A:
    if a > H:
        print(-1)
    elif L <= a <= H:
        print(0)
    elif a < L:
        print(L - a)