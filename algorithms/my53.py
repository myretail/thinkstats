#!/usr/bin/python

# 图的遍历，广度优先

class Note:
    def __init__(self, x, s):
        self.x = x  # 城市编号
        self.s = s  # 转机次数


e = [[99999999 for col in range(51)] for row in range(51)]

e[1][2] = 1
e[2][1] = 1
e[1][3] = 1
e[3][1] = 1
e[2][3] = 1
e[3][2] = 1
e[2][4] = 1
e[4][2] = 1

e[3][4] = 1
e[4][3] = 1

e[3][5] = 1
e[5][3] = 1

e[4][5] = 1
e[5][4] = 1

e[1][1] = 0
e[2][2] = 0
e[3][3] = 0
e[4][4] = 0
e[5][5] = 0

n = 5
m = 7

start = 1
end = 5

book = [0 for col in range(51)]

que = [Note(0,0) for col in range(2501)]

head = 1
tail = 1
que[tail] = Note(start, 0)
tail += 1
book[1] = start
flag=0
while head < tail:
    cur = que[head].x
    for i in range(n):
        j = i + 1
        if e[cur][j] != 99999999 and book[j] == 0:
            que[tail] = Note(j, que[head].s + 1)
            tail += 1
            book[j] = 1

        if que[tail].x == end:
            flag = 1
            break

    if flag == 1:
        break

    head = head + 1

print(que[tail - 1].s)
