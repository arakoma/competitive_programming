N = int(input())
S = list(input())
"""
ans = ""
for a in S:
    ans += chr((ord(a) + N - ord("A")) % 26 + ord("A"))

"""
ans = ""
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for a in S:
    ans += alpha[(alpha.index(a) + N) % 26]

print(ans)