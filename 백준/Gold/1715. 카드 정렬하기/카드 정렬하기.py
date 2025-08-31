import heapq

N = int(input())

cards = [ int(input()) for i in range(N)]

if len(cards)==1:
    print(0)

else:    
    heapq.heapify(cards)
    results = 0
    while len(cards)>=2:
        a = heapq.heappop(cards)
        b = heapq.heappop(cards)

        cost = a+b
        results += cost

        heapq.heappush(cards, cost)
    print(results)    




