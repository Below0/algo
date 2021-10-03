def run():
    while True:
        w, h = map(int, input().split(" "))
        if w == 0 and h == 0:
            break

        answer = 0
        m = [[0 for _ in range(w)] for _ in range(h)]
        visit = [[0 for _ in range(w)] for _ in range(h)]

        def dfs(y, x):
            visit[y][x] = 1
            for i in range(-1, 2):
                for j in range(-1, 2):
                    dx = x + i
                    dy = y + j

                    if w > dx > -1 and h > dy > -1:
                        if visit[dy][dx] == 0 and m[dy][dx] == 1:
                            dfs(dy, dx)

        for i in range(h):
            tmp = list(map(int, input().split()))
            for j, t in enumerate(tmp):
                m[i][j] = t

        for i in range(h):
            for j in range(w):
                if visit[i][j] == 0 and m[i][j] == 1:
                    dfs(i, j)
                    answer += 1

        print(answer)


if __name__ == "__main__":
    run()
