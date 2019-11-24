H, W = map(int,input().split())
A = [input() for _ in range(H)]

print('#' * (W+2))
for ai in A:    
    print('#' + ai + '#')
print('#' * (W+2))