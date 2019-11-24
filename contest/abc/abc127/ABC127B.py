r, D, x = map(int, input().split())

xi = x+0
for i in range(10):
    ans = r * xi -D
    print(ans)
    xi = ans