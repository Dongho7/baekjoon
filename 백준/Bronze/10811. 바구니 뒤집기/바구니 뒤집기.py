N, M = map(int, input().split())
basket = [i for i in range(1, N+1)]

for _ in range(M):
    start, end = map(int, input().split())
    basket[start-1:end] = reversed(basket[start-1:end])  # 슬라이싱 후 바로 뒤집어서 할당

print(*basket)