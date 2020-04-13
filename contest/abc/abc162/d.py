N = int(input())
S = input()

r = S.count("R")
g = S.count("G")
b = S.count("B")

ans = r * g * b

for i in range(1, N-1):
    now = S[i]
    for j in range(1, min(i, N-1-i)+1):
        if len(set([S[i-j], now, S[i+j]])) == 3:
            ans -= 1


print(ans)