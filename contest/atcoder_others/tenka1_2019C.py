#TLE
#毎回countを回すので時間かかる
N = int(input())
S = list(input())

if '#' not in S or '.' not in S:
    ans = 0
else:
    ans = 2*10**5
    for i in range(N):
        ans = min(S[:i].count('#') + S[i:].count('.'), ans)

print(ans)

####################
#値を保持して進めば短くなる
N = int(input())
S = list(input())

white = S.count('.')
black = 0
ans = white + black

for x in S:
    if x == '.':
        white -= 1
    else:
        black += 1
    ans = min(ans, white+black)

print(ans)