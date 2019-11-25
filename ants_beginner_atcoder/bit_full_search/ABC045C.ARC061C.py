# bit全探索
S = input()

ans = 0
for i in range(2**(len(S)-1)):
    formula = ""
    for j in range(len(S)):
        formula += S[j]
        if (i >> j) & 1:
            formula += "+"
    ans += eval(formula)
    #ans += sum(map(int, formula.split("+")))でもOK

print(ans)