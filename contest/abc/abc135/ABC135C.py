N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
x = 0
for i in range(N):
    if A[i] >= (B[i] + x):
        ans += B[i] + x
        x = 0
    if A[i] <= x:
        ans += A[i]
        x = B[i]
    elif A[i] < (B[i] + x):
        ans += A[i]
        x = B[i] - (A[i] - x)
else:
    if A[N] >= x:
        ans += x
    else:
        ans += A[N]

print(ans)

###
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

fi1 = min(A[0], B[0])
fi2 = min(A[1], B[0] - fi1)
ans = fi1 + fi2
for i in range(1, N):
    fi1 = min(A[i] - fi2, B[i])
    fi2 = min(A[i+1], B[i] - fi1)
    ans += fi1 + fi2
    
print(ans)