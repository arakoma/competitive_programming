d, n = map(int, input().split())
if n <= 99:
    print((100**d)*n)
elif n == 100:#このとき100で割れる回数が増えるので例外
    print((100**d)*101)