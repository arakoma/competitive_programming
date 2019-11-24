n, a, b = map(int, input().split())

ans = 0
for i in range(n+1):
    i_sum = 0
    for j in range(len(str(i))):
        i_sum += int(str(i)[j])
    if a <= i_sum <= b:
        ans += i

print(ans)

##########################
#iを文字列にしてからさらにリストにしてmapでintかけて合計
n,a,b = map(int,input().split())
ans = 0
for i in range(1,n+1):
    if(a <= sum(map(int,list(str(i)))) <= b):
        ans += i
print(ans)