a, b = input().split()
ab = int(a+b)

print("Yes" if ab**(1/2)%1==0 else "No")
#平方根はimport mathでsqurtでもいいし
#平方根は1/2乗とみてもいいし

#整数かどうかは、1で割った余りが0かで判定できる