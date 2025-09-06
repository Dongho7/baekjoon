from collections import deque
import sys

input = sys.stdin.readline

def bfs(start_node):
    que = deque([start_node])
    color[start_node] = 1

    while que:
        current = que.popleft()
        visited[current] = True

        for next in connect[current]:
            if color[next] ==0:
                color[next] = 3 - color[current]
                que.append(next)
            elif color[next] == color[current]:
                
                return False
    return True

K = int(input())

result = []
for _ in range(K):
    V, E = map(int, input().split())
    #정점 개수, 간선의 개수
    connect = [[] for i in range(V+1)]
    for i in range(E):
        a, b = map(int, input().split())
        connect[a].append(b)
        connect[b].append(a)

    visited = [False]*(V+1)
    color = [0]*(V+1)
   
    
    flag = True 
    for i in range(1, V+1):
        if color[i] ==0:
            if bfs(i) == False:
                flag = False
    
    if flag ==False:
        result.append("NO")
    else:
        result.append("YES")
print(*result, sep="\n")







            
