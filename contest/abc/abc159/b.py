S = input()

n = len(S)
ans = "No"
if S[:n//2] == S[n//2+1:][::-1]:
    S1 = S[:(n-1)//2]
    n1 = len(S1)
    if S1[:n1//2] == S1[(n1+1)//2:][::-1]:
        S2 = S[(n+3)//2-1:]
        n2 = len(S2)
        if S2[:n2//2] == S2[(n2+1)//2:][::-1]:
            ans = "Yes"

print(ans)