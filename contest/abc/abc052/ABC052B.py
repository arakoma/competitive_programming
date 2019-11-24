N = int(input())
S = input()

x = 0
x_max = 0
for i in range(N):
    if S[i] == 'I':
        x += 1
    elif S[i] == 'D':
        x -= 1
    x_max = max(x_max, x)

print(x_max)