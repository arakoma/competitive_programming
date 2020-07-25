A, B, C = map(int, input().split())
K = int(input())

ans = "No"
def f(a, b, c, cnt, k):
    global ans
    if cnt > k:
        return
    if b > a and c > b:
        ans = "Yes"
        return
    
    f(2*a, b, c, cnt+1, k)
    f(a, 2*b, c, cnt+1, k)
    f(a, b, 2*c, cnt+1, k)


f(A, B, C, 0, K)
print(ans)