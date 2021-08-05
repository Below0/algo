visit = [[0 for i in range(5)] for i in range(5)]
dx = [1, 0, -1 ,0]
dy = [0, 1, 0, -1]

def check(place):
    people = []
    def dfs(x, y, n):
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
        if 0 < tx < 5 and 0 < ty < 5 and visit[x][y] == 0:
            return dfs(tx, ty, n-1)

    for i in range(len(place)):
        idx = 0
        while idx > -1:
            idx = place[i].find( "P")
            print(idx)
            if idx:
                people.append((i, idx))

    print(people)

    return 1



def solution(places):
    result = []
    for place in places:
        result.append(check(place))

    return result

places = ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]
solution(places)
