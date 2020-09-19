S = input()
ans = ""
if S[-1] == "s":
    ans = S + "es"
else:
    ans = S + "s"
print(ans)