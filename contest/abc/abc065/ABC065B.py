N = int(input())
a = [int(input()) for _ in range(N)]

button = 1
for i in range(N):
    if button == 2:
        print(i)
        break
    button = a[button-1]
    
else:
    print(-1)