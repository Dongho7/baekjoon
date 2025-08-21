
N = int(input())

A= list(map(int, input().split()))
dp= A[:]

for i in range(1, N):
    for j in range(i):
        if A[i]>A[j]:
            dp[i] = max(dp[i], A[i] + dp[j])


print(max(dp))