X = int(input())

for a in range(-300, 300):
    for b in range(-300, 300):
        if a ** 5 - b ** 5 == X:
            A = a
            B = b

print(str(A) + " " + str(B))