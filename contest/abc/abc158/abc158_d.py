S = input()
Q = int(input())
query = [list(input().split()) for _ in range(Q)]

cnt = 0
for q in query:
    if q[0] == "1":
        cnt += 1
    
    elif q[0] == "2":
        if cnt % 2 == 0:
            if q[1] == "1":
                S = q[2] + S
            elif q[1] == "2":
                S = S + q[2]
        else:
            if q[1] == "1":
                S = S + q[2]
            elif q[1] == "2":
                S =q[2] + S

if cnt % 2 == 1:
    S = S[::-1]

print(S)