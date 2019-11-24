A = input()
B = input()
C = input()

next_turn = A[0]
Acnt = 1
Bcnt = 0
Ccnt = 0
while True:
    if next_turn == 'a':
        if Acnt == len(A):
            print('A')
            break
        next_turn = A[Acnt]
        Acnt += 1

    elif next_turn == 'b':
        if Bcnt == len(B):
            print('B')
            break
        next_turn = B[Bcnt]
        Bcnt += 1

    elif next_turn == 'c':
        if Ccnt == len(C):
            print('C')
            break
        next_turn = C[Ccnt]
        Ccnt += 1

#####################
s = { 'a':input(), 'b':input(), 'c':input() }
n = 'a'
while True:
    if 0 < len(s[n]):
        o = s[n][0]
        s[n] = s[n][1:]
        n = o
    else:
        print(n.upper())
        break