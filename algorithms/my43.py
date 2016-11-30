#!/usr/bin/python
# 广度优先

import numpy


class Node:
    def __init__(self, x, y, f, s):
        self.x = x
        self.y = y
        self.f = f
        self.s = s


m = 4
n = 5

que = {}

a = [[0 for col in range(51)] for row in range(51)]

book = [[0 for col in range(51)] for row in range(51)]
next = numpy.array([[0, 1], [1, 0], [0, -1], [-1, 0]])

a[1][3] = 1
a[3][3] = 1
a[4][2] = 1
a[5][4] = 1
startx = 1
starty = 1
p = 4
q = 3

head = 1
tail = 1
que[tail] = Node(startx, starty, 0, 0)
tail = tail + 1
book[startx][starty] = 1
flag = 0

while head < tail:
    for k in range(4):

        tx = que[head].x + next[k][0]
        ty = que[head].y + next[k][1]

        if tx < 1 or tx > n or ty < 1 or ty > m:
            continue
        if a[tx][ty] == 0 and book[tx][ty] == 0:
            book[tx][tx] = 1
            que[tail] = Node(tx, ty, head, que[head].s + 1)
            tail = tail + 1

        if tx == p and ty == q:
            flag = 1
            break

    if flag == 1:
        break

    head = head + 1

print("{0}".format(que[tail - 1].s))
