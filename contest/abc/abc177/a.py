D, T, S = map(int, input().split())

ans = "No"
if D / S <= T:
    ans = "Yes"

print(ans)