a, b = input().split()
sa = sum(list(map(int, list(a))))
sb = sum(list(map(int, list(b))))
if sa > sb:
    print(sa)
else:
    print(sb)