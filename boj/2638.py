def run():
    N, M = map(int, input().split())

    m = []
    for _ in range(N):
        lst = list(map(int, input().split()))
        m.append(lst)

    print(m)


if __name__ == "__main__":
    run()
