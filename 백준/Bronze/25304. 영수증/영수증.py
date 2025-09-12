total =int(input())

N= int(input())

sum = 0
for i in range(N):
    price_per_unit, q = map(int, input().split())
    price = price_per_unit*q
    sum += price

if total == sum:
    print("Yes")
else:
    print("No")