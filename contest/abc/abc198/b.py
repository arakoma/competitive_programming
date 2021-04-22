n = input()
ans = "No"
for i in range(20):
    s = "0"*i + n
    if s == s[::-1]:
        ans = "Yes"
print(ans)