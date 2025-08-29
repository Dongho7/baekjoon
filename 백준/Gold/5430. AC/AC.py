from collections import deque
K = int(input())
for _ in range(K):
    do_origin = input()
    N=int(input())

    array = input()
    if N == 0:
        que = deque()
    else:
        que = deque(map(int, array[1:-1].split(",")))  

    flag = True # True는 정방향, False 는 뒤집기
    error = False
    for i in do_origin:
        if i == "R":
            flag = not flag#역방향으로 바꿔주기 (대신에 하드코딩 하지 말고, 토글 형식으로 바꿔주기)
        elif i == "D":
            if not que:
                print("error")
                error = True
                break
            else:
                if flag == True:
                    que.popleft()
                elif flag == False:
                    que.pop()

    if not error:
        if not flag:
            que.reverse()
        print("["+ ",".join(map(str, que)) +"]"  )

    



