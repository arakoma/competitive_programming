A, B, C = map(int, input().split())

sum_A = A
for i in range(B):
    sum_A += A
    if sum_A % B == C:
        print("YES")
        break
else:
    print("NO")