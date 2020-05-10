S = input()
T = input()

ans = "No"
if S == T[:-1]:
    ans = "Yes"

print(ans)