from collections import deque
M, N, K = map(int, input().split())
#세로 , 가로, 색칠된 사각형 개수

maps = []

for i in range(M):
    row = [0]*N
    maps.append(row)


for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for k in range(y1, y2): #y1 부터 (y2-y1-1) 만큼 range 돌려
        #x1 부터 (x2-x1-1) 만큼 range 돌려
        for j in range(x1, x2):
            maps[k][j] = 1


mv_col = [-1, 1, 0, 0]
mv_row = [0, 0, -1, 1]

visited_array = [[False]*N for i in range(M)]

def bfs(x,y):
    que = deque()
    que.append((x,y))
    visited_array[y][x] = True
    area = 1

    while que:
        nx, ny = que.popleft()
        for i in range(4):
            new_x = nx + mv_col[i]
            new_y = ny + mv_row[i]
            if 0 <= new_x < N and 0 <= new_y < M:
                if visited_array[new_y][new_x] == False and maps[new_y][new_x] != 1:
                    visited_array[new_y][new_x] = True 
                    area += 1
                    que.append((new_x, new_y))
    return area

count = 0
area_list = []
for i in range(M):
    for j in range(N):
        if visited_array[i][j] == False and maps[i][j] != 1:
            area_list.append(bfs(j, i))
            count +=1 

area_list.sort()
print(count)
print(*area_list)