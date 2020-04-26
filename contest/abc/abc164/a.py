S, W = map(int, input().split())
ans = "safe"
if W >= S:
    ans = "unsafe"

print(ans)