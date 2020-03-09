A, B = map(int, input().split())

ans = -1
for i in range(10000):
    if i * 8 // 100 == A:
        if i * 10 // 100 == B:
            ans = i
            break

print(ans)

"""
# floor(N*0.08) == A を変形して
# N*0.08-1 < A <= N*0.08
# Nについて整理すると
# A*100/8 <= N < (A+1)*100/8
# Bについても同様にすると、まとめてx <= N < y とできる


A, B = map(int, input().split())

x = max((A*100+7)//8, B*100//10)
y = min((A+1)*100/8, (B+1)*100/10)

if x < y:
    ans = x
else:
    ans = -1

print(ans)
"""