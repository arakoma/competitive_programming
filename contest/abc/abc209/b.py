n, x = map(int, input().split())
A = list(map(int, input().split()))

for i in range(n):
    if i%2==0:
        x -= A[i]
    else:
        x -= A[i]-1

if x >= 0:
    print("Yes")
else:
    print("No")