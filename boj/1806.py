N, M = map(int, input().split())

arr = list(map(int, input().split()))

start, end = 0, 0
tmp = 0

MIN = 100001
ptr_len = 0

while end < N:
    tmp += arr[end]

    while tmp >= M and start < end:
        ptr_len = end - start + 1
        if ptr_len < MIN:
            MIN = ptr_len
        tmp -= arr[start]
        start += 1

    end += 1

print(MIN)