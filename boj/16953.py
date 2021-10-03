from collections import deque


def bfs(A, B):
    q = deque()
    INF = 10 ** 9 + 1
    v = set()

    q.append(A)
    cnt = 0
    while q:
        for i in range(len(q)):
            t = q.popleft()
            v.add(t)

            if t == B:
                return cnt

            tmp = 2 * t

            if tmp <INF and tmp not in v:
                q.append(tmp)

            tmp = int(str(t) + "1")
            if tmp < INF and tmp not in v:
                q.append(tmp)

        cnt += 1

    return -1


def run():
    A, B = map(int, input().split())
    res = bfs(A, B)
    if res != -1:
        res += 1

    print(res)


if __name__ == "__main__":
    run()
