S = input()

M1 = False
M2 = False
if int(S[0]) <= 1:
    if S[0] == '0' and S[1] != '0':
        M1 = True
    elif S[0] == '1':
        if 0 <= int(S[1]) <= 2:
            M1 = True

if int(S[2]) <= 1:
    if S[2] == '0' and S[3] != '0':
        M2 = True
    elif S[2] == '1':
        if 0 <= int(S[3]) <= 2:
            M2 = True

if M1 and M2:
    print("AMBIGUOUS")
elif M1 and (not M2):
    print("MMYY")
elif (not M1) and M2:
    print("YYMM")
elif (not M1) and (not M2):
    print("NA")