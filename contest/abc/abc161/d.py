from collections import deque


K = int(input())

d = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])

for _ in range(K-1):
    x = d.popleft()
    # x の1桁目を見る
    mod = x % 10
    if mod != 0:
        d.append(10 * x + mod - 1)
    d.append(10 * x + mod)
    if mod != 9:
        d.append(10 * x + mod + 1)

ans = d.popleft()
print(ans)