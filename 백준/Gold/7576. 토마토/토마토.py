from collections import deque

M, N = map(int, input().split())   # 가로 M, 세로 N
box = [list(map(int, input().split())) for _ in range(N)]

# 방향 (상, 하, 좌, 우)
d_row = [-1, 1, 0, 0]  # 세로 이동 
d_col = [0, 0, -1, 1]  # 가로 이동 

visited = [[False]*M for _ in range(N)]

def bfs():
    que = deque()
    # 모든 익은 토마토를!!!!
    for row in range(N):
        for col in range(M):
            if box[row][col] == 1:
                que.append((row, col))
                visited[row][col] = True

    while que:
        row, col = que.popleft()
        for i in range(4):
            nrow = row + d_row[i]
            ncol = col + d_col[i]
            if 0 <= nrow < N and 0 <= ncol < M:
                if box[nrow][ncol] == 0 and not visited[nrow][ncol]:
                    visited[nrow][ncol] = True
                    box[nrow][ncol] = box[row][col] + 1
                    que.append((nrow, ncol))

bfs()

# 결과 계산
ans = 0
for row in box:
    for val in row:
        if val == 0: 
            print(-1)
            exit()
    ans = max(ans, max(row))

print(ans - 1)
