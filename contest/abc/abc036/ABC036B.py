N = int(input())
s = [input() for _ in range(N)]

ans = []
for i in range(N):
    in_ans = ""
    for j in range(N):
        in_ans += s[N-j-1][i]
    else:
        ans.append(in_ans)

for x in ans:
    print(x)


######################
N = int(input())
s = [input() for _ in range(N)]

for i in range(N):
    ans = ""
    for j in range(N):
        ans += s[N-j-1][i]
    else:
        print(ans)