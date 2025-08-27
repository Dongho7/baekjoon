import sys
import heapq

input = sys.stdin.readline
n = int(input())

heap = []

for _ in range(n):
    x = int(input())
    if x != 0:
        # (절댓값, 실제값) 형태로 넣는다
        heapq.heappush(heap, (abs(x), x))
    else:
        if heap:
            # 절댓값 기준 최소, 같으면 실제값이 작은 것
            print(heapq.heappop(heap)[1])
        else:
            print(0)
