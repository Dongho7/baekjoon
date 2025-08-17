# 6
# 0 dp[0] #출발
 # 10 dp[1]
  # 20 dp[2] #MAX: 30
   # 15 dp[3] #MAX : dp[3] = dp[2] + stair[3]
    # 25 dp[4] #MAX : dp[4] = 
     # 10 dp[5]
      # 20 dp[6]

# 두 칸 뛰는 것보다 뭐가 더 나은지 max(dp[?], dp[?] 로 판별해야 될 거 같음)
#근데 그냥 다 밟음 되는 거 아님? 하지만.. 연속된 세 개의 계단을 모두 밟아서는 안 된다.
# 

N = int(input())

stair = [0] * (N + 1)
for i in range(1, N + 1):
    stair[i] = int(input()) 
# stair = [0, 10, 20, 15, 25, 10, 20] #6개 계단

dp = [0] * (N + 1)

if N>=1:
    dp[1] = stair[1]
if N>=2:
    dp[2] = stair[1]+stair[2] 
# if N>=3:
#     dp[3] = max(stair[1]+stair[3], stair[2]+stair[3])

for i in range(3, N+1):
    dp[i] = max(dp[i-2] + stair[i],  dp[i-3] + stair[i-1] + stair[i])
    #3일 때, dp[3]은(최댓값)  dp[1]+ stair[3] or dp[0] + stair[2] + stair[3]

print(dp[N])