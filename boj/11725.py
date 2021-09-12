from collections import deque

def run():
    N = int(input())
    m = [[] for _ in range(N)]

    parents = [0 for _ in range(N)]

    for i in range(N-1):
        a, b = map(int, input().split(" "))
        m[a-1].append(b-1)
        m[b-1].append(a-1)

    q = deque()
    visit = set()

    q.append(0)
    visit.add(0)

    while q:
        parent = q.popleft()
        for child in m[parent]:
            if child not in visit:
                parents[child] = parent
                visit.add(child)
                q.append(child)

    for i in range(1, len(parents)):
        print(parents[i] + 1)

run()


if __name__ == "__main__":
    run()
