N = input()
ans = ""
if N[-1] in ("2", "4", "5", "7", "9"):
    ans = "hon"
elif N[-1] in ("0", "1", "6", "8"):
    ans = "pon"
elif N[-1] in ("3"):
    ans = "bon"

print(ans)