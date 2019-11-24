S = list(input())
for i in range(3):
    if S[i] == S[i+1]:
        print("Bad")
        break
else:
    print("Good")