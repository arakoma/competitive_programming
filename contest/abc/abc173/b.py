N = int(input())
S = [input() for _ in range(N)]

C = [0] * 4
for s in S:
    if s == "AC":
        C[0] += 1
    elif s == "WA":
        C[1] += 1
    elif s == "TLE":
        C[2] += 1
    elif s == "RE":
        C[3] += 1

print("AC x " + str(C[0]))
print("WA x " + str(C[1]))
print("TLE x " + str(C[2]))
print("RE x " + str(C[3]))