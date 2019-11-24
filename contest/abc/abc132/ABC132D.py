def p(n):
    if n == 0:
        return 1
    else:
        return n * p(n-1)

N, K = map(int, input().split())

for i in range(1, K+1):
    if i > N-K+1:
        print(0)
        continue
    
    #青の分け方
    x = K - i
    x_div = p(x+i) / (p(x) * p(i-1))

    #赤の分け方
    y_div = 0
    for j in (i-1, i, i+1):
        y = N - K - j
        y_div += p(y) / (p(y) * p(j))

    print(x_div * y_div)