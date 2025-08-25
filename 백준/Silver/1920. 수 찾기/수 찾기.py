import sys
input = sys.stdin.readline


N = int(input())
data = set(map(int, input().split()))

M = int(input())
for_find = list(map(int, input().split()))
opc = []
for i in for_find:
    if i in data:
        opc.append("1")
    else:
        opc.append("0")


print(*opc, sep="\n")