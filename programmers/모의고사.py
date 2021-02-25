def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    p_list = [p1, p2, p3]

    score_list = []

    MAX = -1

    for p in p_list:
        score = 0
        for i in range(len(answers)):
            if answers[i] == p[i % len(p)]:
                score += 1
        if score > MAX:
            MAX = score

        score_list.append(score)

    answer = []

    for i in range(len(score_list)):
        if score_list[i] == MAX:
            answer.append(i + 1)

    return answer