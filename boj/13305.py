def run():
    N = int(input())

    length_lst = list(map(int, input().split(" ")))
    price_lst = list(map(int, input().split(" ")))
    print(price_lst)

    oil = 0
    now = 0
    while now < N:
        next = now + 1

        while next < N -1:
            if price_lst[now] > price_lst[next]:
                break
            next += 1

        print(next)

        now = next
        oil += price_lst[now] * (next - now)
        print(next)

    print(oil)


if __name__ == "__main__":
    run()
