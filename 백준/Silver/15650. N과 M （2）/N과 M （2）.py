N, M = map(int, input().split())

#자연수, 수열의 길이
visited = [False]*(N+1)
pop_list =[]


def dfs(start):
    
    if len(pop_list) == M: # len(pop_list) == 2
        print(*pop_list)
        return



    for i in range(start, N+1): # range(1, 5)
            pop_list.append(i)
            dfs(i+1)
            pop_list.pop()

dfs(1)