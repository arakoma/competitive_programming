N = int(input())
print(N**3)

###
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = 0
a = 9999999
for i in range(N):
    ans += B[A[i]-1]
    if A[i] == a + 1:
        ans += C[a-1]
    a = A[i]

print(ans)

###
N = int(input())
B = list(map(int, input().split()))

ans = B[0]
for i in range(N-2):
    ans += min(B[i], B[i+1])
else:
    ans += B[-1]

print(ans)

###
N, K = map(int, input().split())
S = input()

happy = 0
for i in range(N-1):
    if S[i] == S[i+1]:
        happy += 1

print(min(N-1, happy+2*K))