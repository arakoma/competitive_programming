n = input()

nsum = 0
for i in range(len(n)):
    nsum += int(n[i])

if int(n) % nsum == 0:
    print("Yes")
else:
    print("No")