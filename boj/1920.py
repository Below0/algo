from math import floor


def binary_search(lst, target):
    left = 0
    right = len(lst) - 1

    while left < right:
        print(f"{left}, {right}")

        idx = floor((right + left) / 2)
        mid = lst[idx]
        print(mid)

        if mid == target:
            return idx
        elif mid > target:
            right = idx - 1
        else:
            left = idx + 1

    return -1


def run():
    N = int(input())
    n_list = list(map(int, input().split(" ")))

    M = int(input())
    m_list = list(map(int, input().split(" ")))

    n_list.sort()

    for m in m_list:
        res = binary_search(n_list, m)
        if res >= 0:
            print(1)
        else:
            print(0)


if __name__ == "__main__":

