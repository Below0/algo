import sys

lst = [0] * 10000

N = int(input())

for i in range(N):
    idx = int(sys.stdin.readline())
    lst[idx-1] += 1

for i in range(10000):
    if lst[i] == 0:
        continue

    for j in range(lst[i]):
        print(i+1)


