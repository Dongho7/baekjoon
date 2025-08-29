from collections import Counter

N=int(input())
list1 = list(map(int, input().split()))
M = int(input())
list2 = list(map(int, input().split()))

counts = Counter(list1)
result = [counts[i] for i in list2]
print(*result)