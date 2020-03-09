S = input()
ans = "No"
if len(S) % 2 == 0:
    if S == ("hi" * (len(S) // 2)):
        ans = "Yes"


print(ans)