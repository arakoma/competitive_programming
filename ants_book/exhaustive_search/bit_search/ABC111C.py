n = int(input())
v = list(map(int, input().split()))

even = {}
odd = {}

# iは0から
for i in range(n):
    if i % 2 == 0:
        if v[i] not in even:
            even[v[i]] = 0
        even[v[i]] += 1
    else:
        if v[i] not in odd:
            odd[v[i]] = 0
        odd[v[i]] += 1

even_sorted = sorted(even.items(), key=lambda x:x[1])[::-1]
odd_sorted = sorted(odd.items(), key=lambda x:x[1])[::-1]

ans = 0
if even_sorted[0][0] != odd_sorted[0][0]:
    ans += n - even_sorted[0][1] - odd_sorted[0][1]
else:
    if len(even_sorted) == 1 or len(odd_sorted) == 1:
        even_sorted.append((-1, 0))
        odd_sorted.append((-1, 0))
    x = n - even_sorted[0][1] - odd_sorted[1][1]
    y = n - even_sorted[1][1] - odd_sorted[0][1]
    ans += min(x, y)

print(ans)


###############
'''https://atcoder.jp/contests/abc111/submissions/7322974'''
###############
n = int(input())
nums = list(map(int, input().split()))

nums1 = nums[0::2]
nums2 = nums[1::2]

bug1 = [0] * 100001
bug2 = [0] * 100001

for num in nums1:
    bug1[num] += 1

for num in nums2:
    bug2[num] += 1

max_v_1 = max(bug1)
max_i_1 = bug1.index(max_v_1)
max_v_2 = max(bug2)
max_i_2 = bug2.index(max_v_2)

if max_i_1 == max_i_2:
    bug1[max_i_1] = 0
    bug2[max_i_2] = 0
    sec_max_v_1 = max(bug1)
    sec_max_v_2 = max(bug2)
    print(n - max(max_v_1, max_v_2) - max(sec_max_v_1, sec_max_v_2))
else:
    print(n - max_v_1 - max_v_2)
