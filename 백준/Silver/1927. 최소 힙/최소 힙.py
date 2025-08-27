import heapq
import sys

input = sys.stdin.readline

N = int(input())
#연산 횟수 
heap = []
answer = []

for i in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(heap, x)
    else:
        if heap:
            answer.append(heapq.heappop(heap))
        else:
            answer.append(0)
            
print(*answer, sep="\n")
