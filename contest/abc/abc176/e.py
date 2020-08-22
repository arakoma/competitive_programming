import copy


H, W, M = map(int, input().split())
hw1 = [tuple(map(int, input().split())) for _ in range(M)]
hw2 = copy.deepcopy(hw1)
ans1 = 0
ans2 = 0

# hから見る
h_cnt = [0 for _ in range(3*10**5 + 3)]
w_cnt = [0 for _ in range(3*10**5 + 3)]
for h, w in hw1:
    h_cnt[h] += 1
    w_cnt[w] += 1

h_max = -1
h_idx = 999999999999

for i in range(len(h_cnt)):
    if h_cnt[i] > h_max:
        h_max = h_cnt[i]
        h_idx = i
    elif h_cnt[i] == h_max:
        if w_cnt[i] > w_cnt[h_idx]:
            h_idx = i


L = []
for i in range(len(hw1)):
    h, w = hw1[i]
    if h == h_idx:
        ans1 += 1
        L.append(hw1[i])

hw1 = list(set(hw1) - set(L))

w_cnt = [0 for _ in range(3*10**5 + 3)]
for h, w in hw1:
    w_cnt[w] += 1

w_max = -1
w_idx = 999999999999
for i in range(len(w_cnt)):
    if w_cnt[i] > w_max:
        w_max = w_cnt[i]
        w_idx = i

for h, w in hw1:
    if w == w_idx:
        ans1 += 1


# wから見る
w_cnt = [0 for _ in range(3*10**5 + 3)]
h_cnt = [0 for _ in range(3*10**5 + 3)]

for h, w in hw2:
    h_cnt[w] += 1

w_max = -1
w_idx = 999999999999

for i in range(len(w_cnt)):
    if w_cnt[i] > w_max:
        w_max = w_cnt[i]
        w_idx = i
    elif w_cnt[i] == w_max:
        if h_cnt[i] > h_cnt[w_idx]:
            w_idx = i


L = []
for i in range(len(hw2)):
    h, w = hw2[i]
    if w == w_idx:
        ans2 += 1
        L.append(hw2[i])

hw2 = list(set(hw2) - set(L))

h_cnt = [0 for _ in range(3*10**5 + 3)]
for h, w in hw2:
    h_cnt[h] += 1

h_max = -1
h_idx = 999999999999
for i in range(len(h_cnt)):
    if h_cnt[i] > h_max:
        h_max = h_cnt[i]
        h_idx = i
for h, w in hw2:
    if h == h_idx:
        ans2 += 1


print(max(ans1, ans2))
