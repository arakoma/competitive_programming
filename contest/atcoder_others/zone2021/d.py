s = input()
t = ""
f = [-1, 0]
n = 0
for i in range(len(s)):
    if s[i] == "R":
        n = (n+1) % 2
    elif t != "" and s[i] == t[f[n]]:
        if n == 0:
            t = t[:-1]
        else:
            t = t[1:]
    else:
        if n == 0:
            t = t + s[i]
        else:
            t = s[i] + t

if n == 1:
    t = t[::-1]
print(t)