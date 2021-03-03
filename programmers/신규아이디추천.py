def step1(id):
    new_id = ""
    filter_list = ['-', '_', '.']
    for i in range(len(id)):
        asc = ord(id[i])
        if 65 <= asc <= 90:
            asc += 32
            new_id += chr(asc)

        elif 97 <= asc <= 122 or 48 <= asc <= 57:
            new_id += id[i]

        elif id[i] in filter_list:
            new_id += id[i]

    return new_id


def step2(id):
    new_id = ""
    check = 0

    for i in range(len(id)):
        if id[i] == '.':
            check = 1
        else:
            if check == 1:
                new_id += '.'
                check = 0

            new_id += id[i]

    return new_id


def step3(id):
    if len(id) == 0:
        return id

    if id[0] == '.':
        id = id[1:]

    if id[-1] == '.':
        id = id[:-1]

    return id


def step4(id):
    id_length = len(id)

    if id_length == 0:
        return "a"

    elif id_length >= 16:
        new_id = id[:15]

        while new_id[-1] == '.':
            new_id = new_id[:-1]

        return new_id

    return id

def step5(id):
    while len(id) < 3:
        id += id[-1]

    return id


def solution(new_id):
    answer = new_id
    step_list = [step1, step2, step3, step4, step5]

    for f in step_list:
        answer = f(answer)

    return answer

if __name__ == '__main__':
    print(solution("z-+.^."))

