N = input()
if len(N) == 1:
    print(N)
elif len(N) == 2:
    print(9)
elif len(N) == 3:
    print(9 + int(N[0])*100 - 100 + int(N[1:]) + 1)
elif len(N) == 4:
    print(9 + 900)
elif len(N) == 5:
    print(9 + 900 + 10000*int(N[0]) - 10000 + int(N[1:]) + 1)
elif len(N) == 6:
    print(9 + 900 + 90000)