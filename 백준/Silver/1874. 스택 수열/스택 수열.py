import sys
input = sys.stdin.readline

N = int(input().strip())


ingredient = []
for i in range(N):
    ingredient.append(int(input().strip()))


stack = []
ops  =[]
count = 1

for i in ingredient:
    while count <= i:
        stack.append(count)
        ops.append("+")
        count +=1
    if stack[-1] != i:
        print("NO")
        sys.exit(0)
        
    stack.pop()
    ops.append("-")
    
print('\n'.join(ops))
