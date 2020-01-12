N = int(input())
S = input()

ans = 0
for i in range(N-2):
    if S[i] == "A":
        if S[i+1] == "B":
            if S[i+2] == "C":
                ans += 1

print(ans)