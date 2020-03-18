A, B, K = map(int, input().split())

for i in range(K):
    if i % 2 == 0 and A > 0:
        if A % 2 == 1:
            A -= 1
        B += A // 2
        A //= 2
    
    if i % 2 == 1 and B > 0:
        if B % 2 == 1:
            B -= 1
        A += B // 2
        B //= 2

print(str(A) + " " + str(B))