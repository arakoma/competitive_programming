n, m, x = map(int, input().split())
a = list(map(int, input().split()))

left = 0
for i in range(x):
    if i in a:
        left += 1

right = 0
for j in range(x, n):
    if j in a:
        right += 1

print(min(left, right))

##################################
n, m, x = map(int, input().split())
a = list(map(int, input().split()))

left = len(set(range(0, x)) & set(a))
right = len(set(range(x, n)) & set(a))

print(min(left, right))

##############################
n, m, x = map(int, input().split())
a = list(map(int, input().split()))

b = len(set(range(0, x)) & set(a))

print(min(b, m-b))