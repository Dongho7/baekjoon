from itertools import combinations
from collections import deque
import copy

N, M = map(int, input().split())
laboratory = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 빈칸과 바이러스 좌표 미리 저장
empty = []
virus = []
for i in range(N):
    for j in range(M):
        if laboratory[i][j] == 0:
            empty.append((i, j))
        elif laboratory[i][j] == 2:
            virus.append((i, j))

def bfs(lab):
    q = deque(virus)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if lab[nx][ny] == 0:
                    lab[nx][ny] = 2
                    q.append((nx, ny))

    safe = sum(row.count(0) for row in lab)
    return safe

answer = 0
for walls in combinations(empty, 3):
    # 연구소 복사본 생성
    lab_copy = copy.deepcopy(laboratory)
    # 벽 세우기
    for x, y in walls:
        lab_copy[x][y] = 1
    # 바이러스 퍼뜨리고 안전영역 계산
    answer = max(answer, bfs(lab_copy))

print(answer)
