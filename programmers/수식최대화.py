import itertools

op_list = ['-', '*', '+']


def calc(a, b, op):
    if op == '-':
        return a-b
    elif op == '+':
        return a+b
    elif op == '*':
        return a*b


def find_op(lst, op):
    for i in range(len(lst)):
        if lst[i] == op:
            return i

    return -1


def calc_all(token_list, op):

    while find_op(token_list, op) > -1:
        pos = find_op(token_list, op)
        a = token_list[pos - 1]
        b = token_list[pos + 1]
        token_list[pos] = calc(a, b, op)

        del token_list[pos + 1]
        del token_list[pos - 1]

    return token_list


def calc_simulation(token_list, w_list):
    for op in w_list:
        token_list = calc_all(token_list, op)

    return token_list[0]


def solution(expression):
    answer = 0
    start = 0

    token_list = []
    for i in range(len(expression)):
        token = expression[i]

        if token in op_list:
            token_list.append(int(expression[start:i]))
            token_list.append(token)
            start = i+1

    token_list.append(int(expression[start:]))

    MAX = -1
    for w_list in list(itertools.permutations(op_list, 3)):
        ans = abs(calc_simulation(token_list[:], w_list))
        if ans > MAX:
            MAX = ans

    answer = MAX

    return answer

if __name__ == '__main__':
    print(solution("50*6-3*2"))