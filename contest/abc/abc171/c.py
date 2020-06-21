def xxx(n):
    ans = ""
    i = 1

    while True:
        if n <= 26 ** i:
            n -= 1
            for j in range(i):
                ans = chr(ord("a") + n%26) + ans
                n //= 26
            return ans
        else:
            n -= 26 ** i
            i += 1


N = int(input())
print(xxx(N))