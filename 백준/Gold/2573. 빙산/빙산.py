from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]



def bfs(i, j, visited_array):
    que = deque()
    que.append((i, j))
    visited_array[i][j] = True

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<= nx < N and 0<= ny < M:
                if ice[nx][ny] > 0 and visited_array[nx][ny]==False:
                    que.append((nx,ny))
                    visited_array[nx][ny] = True

icebergs = [(i, j) for i in range(N) for j in range(M) if ice[i][j] > 0]    

def melt():
    melt_array = [[0]*M for _ in range(N)]
    for x, y in icebergs:
        count = 0
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if 0 <= nx < N and 0 <= ny < M and ice[nx][ny] == 0:
                count += 1
        melt_array[x][y] = count

    new_icebergs = []
    for x, y in icebergs:
        ice[x][y] = max(0, ice[x][y] - melt_array[x][y])
        if ice[x][y] > 0:
            new_icebergs.append((x, y))
    return new_icebergs



year = 0

while True:
    count = 0     
    visited_array = [[False]*M for _ in range(N)]
    for x, y in icebergs:
        if ice[x][y]>0 and visited_array[x][y]==False:
            count +=1 
            bfs(x, y, visited_array)

    if count == 0:
        print(0)
        break

    if count >=2:
        print(year)
        break
    icebergs = melt()
    year +=1 

