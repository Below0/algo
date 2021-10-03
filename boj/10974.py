def run():
    N, K = map(int, input().split())
    lst = [1]

    for i in range(2, N+1):
        if N % i == 0:
            lst.append(i)

    if len(lst) < K:
        print(0)
    else:
        print(lst[K-1])


if __name__ == "__main__":
    run()
