from collections import deque
import sys 
M, N, H = map(int, input().split())
#가로, 세로, 높이
input= sys.stdin.readline

box = []

for h in range(H):
    layer = []
    for i in range(N):
        layer.append(list(map(int, input().split())))
    box.append(layer)

que = deque()

for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] ==1:
                que.append((h, n, m))

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
            
def bfs():             
    while que:
        z, x, y = que.popleft()
        for k in range(6):
            nz, nx, ny = z + dz[k] , x+dx[k], y+dy[k]
            if 0<=nz<H and 0<=nx<N and 0<=ny<M:
                if box[nz][nx][ny] == 0:
                    box[nz][nx][ny] = box[z][x][y] + 1
                    que.append((nz, nx, ny))

bfs()

result = 0 

for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 0: 
                print(-1)
                exit(0)
            else: 
                result = max(result, box[h][n][m])

print(result-1)


