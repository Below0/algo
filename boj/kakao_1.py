class Table:
    def __init__(self, n, k):
        self.init_rows = n
        self.rows = n
        self.status = k
        self.stack = []

    def move(self, x):
        self.status += x
        if self.status < 0:
            self.status = 0
        elif self.status > self.rows - 1:
            self.status = self.rows - 1

    def delete(self):
        self.stack.append(self.status)
        if self.status == self.rows - 1:
            self.status -= 1
        self.rows -= 1

    def undo(self):
        undo_item = self.stack.pop()
        self.rows += 1
        if undo_item >= self.status:
            self.status += 1

    def return_answer(self):
        answer_table = ['O' for i in range(self.init_rows)]
        for delete_idx in self.stack:
            answer_table[delete_idx] = 'X'

        answer = ''.join(answer_table)

        return answer


def solution(n, k, cmd):
    """
    :param n:행개수
    :param k:첫 위치
    :param cmd: 커맨드 배열
    :return: 상태 비교
    """
    answer = ''
    table = Table(n, k)
    for command in cmd:
        tokens = command.split(' ')
        if tokens[0] == 'U' or tokens[0] == 'D':
            idx = int(tokens[1])
            if tokens[0] == 'U':
                idx *= -1
            table.move(idx)

        elif tokens[0] == 'C':
            table.delete()
        elif tokens[0] == 'Z':
            table.undo()
    print(table.return_answer())
    return answer

n = 8
k = 2
cmd = []
cmd.append("D 2")
cmd.append("C")
cmd.append("U 3")
cmd.append("C")
cmd.append("D 4")
cmd.append("C")
cmd.append("U 2")
cmd.append("Z")
cmd.append("Z")
solution(n, k, cmd)