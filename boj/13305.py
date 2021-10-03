def run():
    N = int(input())

    length_lst = list(map(int, input().split(" ")))
    price_lst = list(map(int, input().split(" ")))

    oil = price_lst[0]
    now = length_lst[0] * oil

    for i in range(1, N - 1):
        if oil > price_lst[i]:
            oil = price_lst[i]

        now += length_lst[i] * oil

    print(now)


if __name__ == "__main__":
    run()
