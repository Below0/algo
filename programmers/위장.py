import itertools

def solution(clothes):
    answer = 1
    dic = {}

    for item in clothes:
        name, c_type = item
        cnt = dic.get(c_type, 1)
        dic[c_type] = cnt + 1

    for comb in dic.keys():
        answer *= dic[comb]

    return answer - 1
