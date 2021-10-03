def run():
    T = int(input())
    for _ in range(T):
        a, b = map(int, input().split(" "))
        num = pow(a, b, 10)
        if num == 0:
            print(10)
        else:
            print(num)


if __name__ == "__main__":
    run()
