m = int(input()) / 1000
vv = 0

if 0.1 <= m <= 5:
    vv = m * 10
elif 6 <= m <= 30:
    vv = m + 50
elif 35 <= m <= 70:
    vv = (m-30)//5+80
elif 70 < m:
    vv = 89

print(str(int(vv)) if 10<=vv else "0"+str(int(vv)))