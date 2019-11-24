N = int(input())
if N%2==0:
    print(N//2-1)
else:
    print(N//2)

###
N = int(input())
D = list(map(int, input().split()))

if D[0] != 0:
    print(0)
else:
    D.sort()

    if D[1] == 0:
        print(0)
    else:
        mod = 998244353
        ans = 1
        distance = 0
        prev = 1
        now = 0

        for i in range(N):
            if D[i] == distance:
                now += 1
            elif D[i] == distance + 1:
                ans = (ans % mod) * (prev ** now % mod) % mod
                prev = now+0
                now = 1
                distance += 1
            else:
                ans = 0
                break
        else:
            ans = (ans % mod) * (prev ** now % mod) % mod
        
        print(ans)