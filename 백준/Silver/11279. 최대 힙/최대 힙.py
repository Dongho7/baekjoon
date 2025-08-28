import heapq
import sys

input = sys.stdin.readline

heap = []
result = []
N = int(input())
# 연산 횟수 

for i in range(N):
    x = int(input())
    if x !=0:
        heapq.heappush(heap, -1*x)
    else:
        if heap:
            result.append(-heapq.heappop(heap))
        else:
            result.append(0)

print(*result, sep="\n")
