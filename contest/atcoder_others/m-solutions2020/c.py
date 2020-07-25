N, K = map(int, input().split())
A = list(map(int, input().split()))

idx = 0
for i in range(K, N):
    if A[idx] < A[i]:
        ans = "Yes"
    else:
        ans = "No"
    print(ans)

    idx += 1