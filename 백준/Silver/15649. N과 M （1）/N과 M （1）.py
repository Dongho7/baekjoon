N, M = map(int, input().split())

visited = [False] *(N+1)
path = []

def dfs():
    if len(path) == M:
        print(*path)
        return 
    

    for i in range(1, N+1):
        if visited[i]==False:

            visited[i] = True
            path.append(i)

            dfs()

            path.pop()
            visited[i] = False

dfs()