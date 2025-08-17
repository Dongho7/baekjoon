N = int(input())

array = [0] * (N + 1)

for i in range(2, N+1):
    array[i] = array[i-1]+1 # i에서 1을 빼주면 i-1이 되잖아. i-1에서의 최소 횟수를 그대로 가져오는 거지. 근데 거기에서 -1 이 있으니까 횟수 차원에서 1을 더해준 거.
    #가령 빼기 1만 있는 경우를 생각해보자. 5일 떄 1까지 가는 최소의 경우의 수는,.. 결국 4에서 1까지 가는 최소의 경로 수에서 1더 해준 거 잖아.

    #근데 여기는 나누기도 같이 비교를 해야 돼 . 
    if i % 2 == 0: #2로 나눠지면 array[i]
        array[i] = min(array[i], array[i//2]+1) #위에서 구한 array[i]와 array[i//2] + 1을 비교해봐서 더 작은 쪽을 선택해야겠지

    if i % 3 == 0: #3로 나눠지면 array[i]  
        array[i] = min(array[i], array[i//3]+1)


print(array[N])