from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())

relationship = [[] for i in range(N+1)]

for i in range(1, M+1): # 0 - 4
    a, b = map(int, input().split()) # 3, 1
    relationship[b].append(a)

def bfs(V, visited_):
    que = deque([V])
    visited_[V]=True
    count =0

    while que:
        current = que.popleft()
        for new in relationship[current]:
            if visited_[new] == False:
                visited_[new] = True
                que.append(new)
                count +=1
    return count

count =[]
for i in range(1, N+1):
    visited_ = [False]*(N+1)
    if visited_[i] == False:
        count.append((i, bfs(i, visited_)))


value =[]
for _, y in count:
    value.append(y)
max_value =max(value)

result = []
for x,y in count:
    if y ==max_value:
        result.append(x)

print(*result)




#컴퓨터 대수 . 관계의 수