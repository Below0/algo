from collections import deque


def run():
    N = int(input())
    r1, c1, r2, c2 = map(int, input().split())

    d = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]

    q = deque()
    visit = [[-1] * N for _ in range(N)]

    q.append((r1, c1))
    visit[r1][c1] = 0
    cnt = 0
    while q:
        r, c = q.popleft()

        if r == r2 and c == c2:
            break

        for dr, dc in d:
            tr = dr + r
            tc = dc + c

            if N > tr > -1 and N > tc > -1 and visit[tr][tc] == -1:
                q.append((tr, tc))
                visit[tr][tc] = visit[r][c] + 1

        cnt += 1

    print(visit[r2][c2])


if __name__ == "__main__":
    run()
