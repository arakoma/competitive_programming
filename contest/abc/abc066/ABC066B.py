S = list(input())

while True:
    S = S[:-1]
    i = len(S) // 2
    if S[:i] == S[i:]:
        print(len(S))
        break