X, Y, Z = map(int, input().split())
ans = 0
X -= Z
while Y+Z <= X:
    X -= Y+Z
    ans += 1
print(ans)

#####################
#割り算でいいぞ
X, Y, Z = map(int, input().split())
print((X - Z) // (Y + Z))