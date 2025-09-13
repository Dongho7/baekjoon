def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    ans = factorial(M) // (factorial(N) * factorial(M-N))
    print(ans)
