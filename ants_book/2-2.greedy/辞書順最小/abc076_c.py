s = input()
T = input()

slen = len(s)
Tlen = len(T)
ans = "UNRESTORABLE"
if slen >= Tlen:
    for i in range(slen - Tlen + 1)[::-1]:
        for j in range(Tlen):
            if not s[i+j] in ("?", T[j]):
                break
        else:
            ans = s
            ans = ans[:i] + T + ans[i+Tlen:]
            ans = ans.replace("?", "a")
            break

print(ans)
