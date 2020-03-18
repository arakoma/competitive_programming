S = input()
T = input()

flag = False
def dfs(x, y):
    if y >= len(T):
        global flag
        flag = True
        return
    elif not S[x] in (T[y], '?'):
        return
    
    dfs(x+1, y+1)


ans = "UNRESTORABLE"
for i in range(len(S) - len(T) + 1)[::-1]:
    if S[i] in (T[0], '?'):
        dfs(i, 0)
        if flag:
            ans = S[:i] + T + S[i+len(T):]
            ans = ans.replace('?', 'a')
            break

print(ans)