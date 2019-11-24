N, L = map(int, input().split())

azi = []
azi_abs = []
for i in range(N):
    azi.append(i+L)
    azi_abs.append(abs(i+L))

print(sum(azi) - azi[azi_abs.index(min(azi_abs))])