S = input()


for i in range(2**3):
    formula = ""

    for j in range(3):
        formula += S[j]
        if (i >> j) & 1:
            formula += "+"
        else:
            formula += "-"
    formula += S[-1]

    if eval(formula) == 7:
        print(formula + "=7")
        break