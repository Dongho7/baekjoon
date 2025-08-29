K = int(input())

for _ in range(K):
    N=int(input())
    list1 = [input() for i in range(N)]
    list1 = sorted(list1)
    flag = False
    for i in range(len(list1)-1):
        if list1[i+1].startswith(list1[i]):
            flag = True
            break

    if flag ==True:
        print("NO")
    else: 
        print("YES")

