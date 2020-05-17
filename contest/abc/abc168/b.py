K = int(input())
S = input()

ans = ""
if len(S) <= K:
    ans = S
else:
    ans = S[:K] + "..."

print(ans)