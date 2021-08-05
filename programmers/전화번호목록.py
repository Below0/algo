def solution(phone_book):
    s = {n for n in phone_book}

    for phone_num in phone_book:
        for i in range(len(phone_num)):
            num = phone_num[0:i]
            if num in s:
                return False

    return True
