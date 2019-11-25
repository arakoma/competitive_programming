import heapq

N, M = map(int, input().split())
A = list(map(int, input().split()))

#全要素に-1かける
for i in range(len(A)):
    A[i] *= -1

heapq.heapify(A)
for _ in range(M):
    x = heapq.heappop(A)
    heapq.heappush(A, (-x//2)*(-1)) #切り下げのためマイナスを2回かける

print(-sum(A))#全要素を負にしたので戻すためにマイナス付ける

import heapq

heapq.heapify(L) #listをheapに変換
heapq.heappop(L) #最小値を取り出して返す
heapq.heappush(L, a) #heapに要素を追加