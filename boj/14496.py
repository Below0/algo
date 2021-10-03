import heapq, sys


def run():
    a, b = map(int, input().split())
    N, M = map(int, input().split())

    INF = sys.maxsize

    dest = [[] for _ in range(N)]

    hq = []
    answer = [INF] * N
    answer[0] = 0

    for _ in range(M):
        s, e = map(int, input().split())
        dest[s - 1].append(e - 1)
        dest[e - 1].append(s - 1)

    for d in dest[a - 1]:
        answer[d] = 1
        heapq.heappush(hq, d)

    while hq:
        t = heapq.heappop(hq)

        for d in dest[t]:
            if answer[d] > answer[t] + 1:
                answer[d] = answer[t] + 1
                heapq.heappush(hq, d)

    if answer[b-1] >= INF:
        print(-1)
    else:
        print(answer[b - 1])


if __name__ == "__main__":
    run()
