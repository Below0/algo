import heapq


def run():
    N, M, K, X = map(int, input().split())
    INF = 6000000

    road = [[] for _ in range(N)]
    for _ in range(M):
        start, dest = map(int, input().split())
        road[start - 1].append(dest - 1)

    hq = []
    answer = [INF for _ in range(N)]
    answer[0] = 0

    for dest in road[X - 1]:
        answer[dest] = 1
        heapq.heappush(hq, dest)

    while hq:
        t = heapq.heappop(hq)

        for r in road[t]:
            if answer[t] + 1 < answer[r]:
                answer[r] = answer[t] + 1
                heapq.heappush(hq, r)

    a = []
    for i, num in enumerate(answer):
        if num == K:
            a.append(i + 1)

    if len(a) == 0:
        print(-1)
    else:
        for n in a:
            print(n)


if __name__ == "__main__":
    run()
