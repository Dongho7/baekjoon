N = int(input())

dp = [1]*N

A = list(map(int, input().split()))

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1) #max를 쓰는 이유는 , dp[j]+1 만 할 경우 10 20 30 5 60 배열에서 5일 때의 값인 1에다가 1을 더한 2가 선택 됨. 즉 
        #이전까지 쌓아왔던 것들이 다 사라지기 때문에 항상 비교해야 함. i가 30일 때 업데이트한 dp[4]가 선택되게 해야 함

print(max(dp))


