s = input()
li = ["A","T","C","G"]

cnt = 0
cntli = []
for i in range(len(s)):
    if s[i] in li:
        cnt += 1
    else:
        cntli.append(cnt)
        cnt = 0
else:
    cntli.append(cnt)

print(max(cntli))