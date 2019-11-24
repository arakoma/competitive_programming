N = int(input())
A = list(map(int, input().split()))

A.sort()
for i in range(N-1):
    if A[i] <= 0 and A[i+1] <= 0:
        A[i] *= -1
        A[i+1] *= -1
    elif A[i] < A[i+1]*(-1):
        A[i] *= -1
        A[i+1] *= -1

print(sum(A))