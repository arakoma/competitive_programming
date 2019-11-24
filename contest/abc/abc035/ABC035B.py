S = input()
T = int(input())

L_sum = S.count('L')
R_sum = S.count('R')
U_sum = S.count('U')
D_sum = S.count('D')
unknown = S.count('?')

x = abs(L_sum - R_sum)
y = abs(U_sum - D_sum)

if T == 1:
    print(x + y + unknown)
elif T == 2:
    if x+y >= unknown:
        print(abs(x + y - unknown))
    else:
        print(abs((unknown - x - y) % 2))