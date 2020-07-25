D = int(input())#D=365
c = list(map(int, input().split()))#0<=c<=100
s = [list(map(int, input().split())) for _ in range(D)]#0<=s<=20000

t = []
for d in range(D):
    t.append(s[d].index(max(s[d])) + 1)

for i in range(D):
    print(t[i])