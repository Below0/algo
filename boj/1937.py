import copy


def run():
    N = int(input())
    m = []
    MAX = -1

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    visit = [[0 for _ in range(N)] for _ in range(N)]

    def dfs(v, i, j, cnt):
        v[i][j] = 1
        nonlocal MAX

        for k in range(4):
            x = dx[k] + i
            y = dy[k] + j
            if N > x > -1 and N > y > -1:
                if v[x][y] == 0 and m[x][y] > m[i][j]:
                    dfs(v, x, y, cnt + 1)

        visit[i][j] = 0

        if cnt > MAX:
            MAX = cnt

    for i in range(N):
        tree = list(map(int, input().split(" ")))
        m.append(tree)

    for i in range(N):
        for j in range(N):
            dfs(visit, i, j, 1)

    print(MAX)


if __name__ == "__main__":
    run()
