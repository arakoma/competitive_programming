S = input()
N = int(input())
lr = [list(map(int, input().split())) for _ in range(N)]

for l, r in lr:
    S = S[:l-1] + S[l-1:r][::-1] + S[r:]

print(S)