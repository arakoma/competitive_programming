S = input()
a = str(S.count('A'))
b = str(S.count('B'))
c = str(S.count('C'))
d = str(S.count('D'))
e = str(S.count('E'))
f = str(S.count('F'))

print(a+' '+b+' '+c+' '+d+' '+e+' '+f)
#print(*[a,b,c,d,e,f])でいい

##################
s=input()
print(*[s.count(x) for x in 'ABCDEF'])