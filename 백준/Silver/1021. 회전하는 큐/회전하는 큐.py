from collections import deque 

N, M = map(int, input().split())

num_list  = list(map(int, input().split()))
que = deque(range(1, N+1))

count = 0

for i in num_list:
    idx = que.index(i)
    if idx <= len(que) // 2:
        que.rotate(-idx)
        count += idx

    else: 
        que.rotate(len(que)-idx)
        count += (len(que)-idx)

    que.popleft()

print(count)