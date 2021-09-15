from collections import deque


def bfs():
    N, M = map(int, input().split(" "))

    board = [i for i in range(100)]
    visit = [0 for _ in range(100)]

    for i in range(N):
        x, y = map(int, input().split(" "))
        board[x - 1] = y - 1

    for i in range(M):
        u, v = map(int, input().split(" "))
        board[u - 1] = v - 1

    q = deque()
    q.append(0)

    steps = 0
    while q:

        for i in range(len(q)):
            now = q.popleft()
            visit[now] = 1
            print(q)

            if now == 99:
                return steps

            for dice in range(1, 7):
                if now + dice > 99 or visit[board[now + dice]]:
                    continue

                q.append(board[now + dice])

        steps += 1

    return -1


if __name__ == "__main__":
    print(bfs())

