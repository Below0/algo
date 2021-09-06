def run(T):
    btn_time = [300, 60, 10]
    btn_cnt = [0, 0, 0]

    for idx, time in enumerate(btn_time):
        if T >= time:
            cnt = T // time
            T -= time * cnt
            btn_cnt[idx] += cnt

    if T != 0:
        print(-1)
    else:
        for cnt in btn_cnt:
            print(cnt, end=" ")


if __name__ == "__main__":
    T = int(input())
    run(T)
