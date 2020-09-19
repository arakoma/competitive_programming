N = int(input())
D = [list(map(int, input().split())) for _ in range(N)]

ans = "No"
cnt = 0

for i in range(N):
    if len(set(D[i])) == 1:
        cnt += 1
    else:
        cnt = 0
    
    if cnt >= 3:
        ans = "Yes"

print(ans)