N = list(input())
n = 0
for x in N:
    n += int(x)
if n % 9 == 0:
    ans = "Yes"
else:
    ans = "No"
print(ans)