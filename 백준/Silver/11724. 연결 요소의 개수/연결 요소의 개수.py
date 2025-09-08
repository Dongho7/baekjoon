import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

array = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    array[a].append(b)
    array[b].append(a)

visited_bfs = [False] * (N+1)

def bfs(V):
    que = deque([V])
    visited_bfs[V] = True
    while que:
        v = que.popleft()
        for nxt in array[v]:
            if not visited_bfs[nxt]:
                visited_bfs[nxt] = True
                que.append(nxt)

count = 0
for node in range(1, N+1):
    if visited_bfs[node]==False:
        count += 1
        bfs(node)

print(count)
