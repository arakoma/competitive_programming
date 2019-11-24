s = input()

begin = 0
for i in range(len(s)):
    if s[i] == "A":
        begin = i
        break
end = 0
for i in reversed(range(len(s))):
    if s[i] == "Z":
        end = i
        break

print(end - begin + 1)