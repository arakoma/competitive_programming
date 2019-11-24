N = input()
N_sum = 0
for i in range(len(N)):
    N_sum += int(N[i])

print("Yes" if int(N) % N_sum == 0 else "No")

#解説
N = int(input())

t = N + 0
c = 0
while 0 < t:#1の位のみ加算する
    c += t % 10
    t = t // 10

print("Yes" if N % c == 0 else "No")