class calander:
    def __init__(self, e, s, m):
        self.target_e = e - 1
        self.target_s = s - 1
        self.target_m = m - 1
        self.e = 0
        self.s = 0
        self.m = 0
        self.cnt = 1

    def check(self):
        if self.target_e != self.e:
            return False

        if self.target_s != self.s:
            return False

        if self.target_m != self.m:
            return False

        return True

    def up(self):
        self.e = (self.e + 1) % 15
        self.s = (self.s + 1) % 28
        self.m = (self.m + 1) % 19
        self.cnt += 1

    def print(self):
        print(self.cnt, self.e+1, self.s+1, self.m+1)


def run():
    E, S, M = map(int, input().split(" "))
    c = calander(E, S, M)

    while True:
        if c.check():
            return c.cnt
        c.up()


if __name__ == "__main__":
    print(run())
