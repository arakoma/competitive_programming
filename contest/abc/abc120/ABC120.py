a, b, c = map(int, input().split())
print(b//a if b//a <= c else c)

############################################
a, b, k = map(int, input().split())

def ooo(x):
    lix =[]
    for i in range(1, x+1):
        if x % i == 0:
            lix.append(i)
    return lix

lia = ooo(a)
lib = ooo(b)
li = lia + lib

li2 =[]
for n in range(len(li)):
    if not li[n] in li2: 
        if li.count(li[n]) == 2:
            li2.append(li[n])

li2.sort(reverse=True)
print(li2[k-1])
##################################################
s = input()
s2 = s
while "01" in s2 or "10" in s2:
    if "01" in s2:
        s2 = s2.replace("01", "")
    elif "10" in s2:
        s2 = s2.replace("10", "")

print(len(s) - len(s2))

########################################
#############################################

#復習

a,b,c = map(int, input().split())
print(b//a if b//a <= c else c)
#################
a, b, k = map(int, input().split())
li =[]
for i in range(1, min(a, b)+1):
    if a % i == 0 and b % i == 0:
        li.append(i)

print(li[-k])
########################
s = input()
ans = min(s.count("0"), s.count("1")) * 2
print(ans)