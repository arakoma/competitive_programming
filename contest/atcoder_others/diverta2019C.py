N = int(input())
S = [input() for _ in range(N)]

cnt = 0
b = 0
a = 0
ab = 0
for x in S:
    cnt += x.count('AB')
    if x[0] == 'B' and x[-1] == 'A':
        ab += 1
        continue
    if x[0] == 'B':
        b += 1
    if x[-1] == 'A':
        a += 1
    

if (a>0 and b>0) or ab>=2:
    if a==0:
        a = 1
        ab -= 1
    if b==0:
        b = 1
        ab -= 1
    cnt += min(a,b) + ab

print(cnt)