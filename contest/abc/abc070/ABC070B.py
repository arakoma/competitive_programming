a,b,c,d=map(int, input().split())

if b<=c or d<=a:
    ans = 0
elif a<=c:
    if b<=d:
        ans = b-c
    elif d<=b:
        ans = d-c
elif c<=a:
    if d<=b:
        ans = d-a
    elif b<=d:
        ans = b-a
elif a==c and b==d:
    ans = b-a

print(ans)

#############
#min(b,d)-max(a,c)と考えると簡潔に書ける
a, b, c, d = map(int, input().split())

print(max(0, (min(b, d) - max(a,c))))
