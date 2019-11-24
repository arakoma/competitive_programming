S = input()

if S[0] == "A":
    if S[2:-1].count("C") == 1:
        Ssorted = sorted(S)
        if "Z" < Ssorted[2]:#大文字<小文字
            print("AC")
        else:
            print("WA")
    else:
        print("WA")
else:
    print("WA")