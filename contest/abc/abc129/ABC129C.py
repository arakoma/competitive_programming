"""WA
N, M = map(int, input().split())
a = [0] + [int(input()) for _ in range(M)] + [N]

fib = []
for i in range(N+1):
    if i in (0,1):
        fib.append(1)
    else:
        fib.append(fib[i-2] + fib[i-1])

ans = 1
for i in range(1, M+2):
    if (a[i] == 1):
        ans *= 1
    elif  (a[i-1] == N-1):
        ans *= 1
    elif (a[i] - a[i-1] == 1):
        print(0)
        break
    else:
        ans *= fib[a[i]-a[i-1]-1] 
else:
    print(ans% 1000000007)
"""

#1or2歩なので、1段踏まないと、その踏まない床を挟む2つは同じ通りの行き方数をもつ
#具体的には、1,2,3,の床で2を踏まないとき、1から3へは2歩でしか行けない

#踏まない床を0としてフィボナッチ数列を考える
N, M = map(int, input().split())
MOD = 10 ** 9 + 7

arrs = set([int(input()) for _ in range(M)])
anss = [0, 1]
for i in range(1, N+1):
    if i in arrs:
        anss.append(0)
    else:
        anss.append((anss[-2] + anss[-1]) % MOD)
print(anss[-1] % MOD)