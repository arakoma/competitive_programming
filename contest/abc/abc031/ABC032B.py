s = input()
k = int(input())

if k <= len(s):
    s_k = []
    for i in range(len(s)-k+1):
        s_k.append(s[i:i+k])
    print(len(set(s_k)))
else:
    print(0)