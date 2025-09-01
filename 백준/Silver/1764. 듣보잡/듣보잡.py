N, M = map(int, input().split())
listen = {input() for i in range(N)}
see = {input() for i in range(M)}
result = sorted(listen & see)

print(len(result))
print(*result, sep='\n')