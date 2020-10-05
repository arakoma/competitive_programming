N = int(input())
S = input()

cnt = 0

for i in range(1000):
    if 0 <= i < 10:
        a = "00" + str(i)
    elif 10 <= i < 100:
        a = "0" + str(i)
    elif 100 <= i:
        a = str(i)
    
    idx = 0
    for j in range(N):
        if S[j] == a[idx]:
            idx += 1
            if idx == 3:
                cnt += 1
                break

print(cnt)