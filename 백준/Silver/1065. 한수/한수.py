N = int(input())

def is_one_number(x):
    digit = list(map(int, str(x)))
    if len(digit) <=2:
        return True
    else:
        return digit[1] - digit[0] == digit[2]-digit[1]

count = 0
for i in range(1, N+1):
    if is_one_number(i):
        count+=1

print(count)

