from collections import deque 

n = int(input())
a, b = map(int, input().split())
m= int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


visited=[-1]*(n+1)
q = deque([a])
visited[a] = 0

while q:
    cur = q.popleft()
    if cur == b:
        break
    else:
        for i in graph[cur]:
            if visited[i] == -1:
                visited[i] = visited[cur]+1
                q.append(i)

print(visited[b])


