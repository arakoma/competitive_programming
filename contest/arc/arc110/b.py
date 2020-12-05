N = int(input())
T = input()

if "010" in T or "111" in T or "00" in T:
    ans = 0
elif T == "1":
    ans = 2 * 10**10
elif T == "11":
    ans = 10**10
else:
    zeros = N - (sum(map(int, list(T))))
    ans = 10**10 - zeros
    if T[-1] == "0":
        ans += 1

print(ans)