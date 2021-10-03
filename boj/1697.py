from collections import deque


def run():
    m = [0] * 100005
    visit = [0] * 100005
    N, K = map(int, input().split(" "))

    m[K] = 1
    q = deque()
    q.append(N)

    answer = 0
    while q:
        for i in range(len(q)):
            t = q.popleft()
            if m[t] == 1:
                return answer

            if t - 1 >= 0 and visit[t - 1] == 0:
                q.append(t - 1)

            if t + 1 <= 100000 and visit[t + 1] == 0:
                q.append(t + 1)

            if t * 2 <= 100000 and visit[t * 2] == 0:
                q.append(t * 2)

            visit[t] = 1

        answer += 1


if __name__ == "__main__":
    print(run())
