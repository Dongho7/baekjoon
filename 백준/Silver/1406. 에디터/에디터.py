import sys
input = sys.stdin.readline

string = input().strip()
N = int(input())

left = [i for i in string] # a, b, 
right = []
for i in range(N):
    do_ = input().strip()
    if "P" in do_:
        do_, ingredient = do_.split()
        left.append(ingredient)

    if do_ == "L":
        if len(left) > 0:
            right.append(left.pop())
        else:
            pass
    
    if do_ == "D":
        if len(right) > 0:
            left.append(right.pop())

    if do_ == "B":
        if len(left)>0:
            left.pop()


print("".join(left + right[::-1]))

