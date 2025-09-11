N = int(input())

timeline = [[0,0]]
for i in range(1, N+1):
    t, p = map(int, input().split())
    timeline.append([t,p])
dp=[0]*(N+2)

for i in range(1, N+1):
    time, pay = timeline[i]
    dp[i] = max(dp[i], dp[i-1])
    if i + time <= N + 1:
        dp[i + time] = max(dp[i + time], dp[i] + pay)

print(max(dp))
# N = int(input())

# T, P = [0]*(N+1), [0]*(N+1)
# for i in range(1, N+1):
#     t, p = map(int, input().split())
#     T[i], P[i] = t, p

# dp = [0] * (N+2)   # N+1일까지 고려

# for i in range(N, 0, -1):   # N일 → 1일 거꾸로
#     if i + T[i] <= N+1:
#         dp[i] = max(dp[i+1], P[i] + dp[i+T[i]])
#     else:
#         dp[i] = dp[i+1]

# print(dp[1])
