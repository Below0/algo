class Number:
    def __init__(self, n=0):
        self.n = n

    def __repr__(self):
        return self.n

    def apply(self, f):
        if f == '+':
            self.n += 1
        elif f == '-':
            self.n -= 1


class Numbers:
    def __init__(self, n, m, f):
        self.n0 = ''.join(['0' for i in range(6 - len(n))]) + n
        self.m0 = ''.join(['0' for i in range(6 - len(m))]) + m
        self.f = f
        self.f_size = len(f)
        self.cnt = 0

        self.diff = []
        for i in range(6):
            temp_n = int(self.n0[i])
            temp_m = int(self.m0[i])
            self.diff.append(temp_m - temp_n)

    def apply_filter(self, n, reverse = False):
        if reverse:
            f = reversed(self.f)
        else:
            f = self.f
        





    def print_diff(self):
        print(''.join(self.diff))


def run():
    a, b, c = input().split()
    f = input()
    n = Numbers(a, b)
    print(a, b, c, f)
    n.print_diff()


def main():
    t = int(input())
    for i in range(t):
        run()


main()
