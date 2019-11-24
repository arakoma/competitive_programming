N = int(input())

ans = 10**12
for i in range(1, int(N**0.5)+1):
    if N % i == 0:
        ans = min(ans, i + N//i)

print(ans)