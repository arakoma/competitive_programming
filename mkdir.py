import os

N = 104
path = r"contest\arc\arc"
for i in range(1, N):
    if i < 10:
        s = "00" + str(i)
    elif 10 <= i < 100:
        s = "0" + str(i)
    elif 100 <= i < 1000:
        s = str(i)
    
    os.makedirs(path + s)