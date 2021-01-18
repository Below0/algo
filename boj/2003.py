N, M = map(int,input().split())

arr = []
answer = 0

arr = list(map(int, input().split()))

i = 0; j = 0
tmp = 0

while j < len(arr):
    tmp += arr[j]

    while tmp > M:
        tmp -= arr[i]
        i += 1

    if tmp == M:
        answer += 1

    j += 1

print(answer)
