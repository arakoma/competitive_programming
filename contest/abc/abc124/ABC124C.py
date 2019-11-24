#嘘解法
S = list(input())
cnt = 0
for i in range(1,len(S)):
    if S[i-1] == S[i]:
        cnt += 1
        if S[i] == "1":
            S[i] = "0"
        else:
            S[i] = "1"
print(cnt)

####################
S = list(input())
#2パターン考える
ans1 = 0#0101010101010101
ans2 = 0#1010101010101010
for i in range(len(S)):
    if i % 2 == 0:
        if S[i] == "0":#ans1の方は直さなくていいans2を直す
            ans2 += 1
        elif S[i] == "1":#ans2の方は直さなくていいans1を直す
            ans1 += 1
    else:
        if S[i] == "1":#ans1の方は直さなくていいans2を直す
            ans2 += 1
        elif S[i] == "0":#ans2の方は直さなくていいans1を直す
            ans1 += 1

print(min(ans1, ans2))