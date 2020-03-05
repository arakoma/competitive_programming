num = list(map(int, input().split()))
if len(set(num)) == 2:
    print("Yes")
else:
    print("No")