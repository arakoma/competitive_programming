import math
N = int(input())

for i in range(50001):
    if N == math.floor(i * 1.08):
        print(i)
        break
else:
    print(":(")