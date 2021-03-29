N = int(input())
A = list(map(int, input().split()))

ans = 2**30

for i in range(2**(N-1)):
    XOR = 0
    OR = A[0]

    for j in range(N-1):
        if (i >> j) & 1:
            XOR = XOR ^ OR
            OR = A[j+1]
        else:
            OR = OR | A[j+1]
    else:
        XOR = XOR ^ OR
    
    ans = min(ans, XOR)

print(ans)