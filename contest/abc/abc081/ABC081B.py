N = int(input())
A = list(map(int, input().split()))

cnt = 0
while True:
    for i in range(len(A)):
        if A[i] % 2 != 0:
            break #forから抜ける
    else:
        A = [a/2 for a in A]
        cnt += 1
        continue
    break #whileから抜ける

print(cnt)