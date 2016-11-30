#!/usr/bin/python

import numpy


class Node:
    def __init__(self, x, y):
        self.x = x #横坐标
        self.y = y #纵坐标


def getnum(i, j):
    # sum用来计数（可以消灭的敌人数），所以需要初始化为0
    sum = 0
    # 将坐标i,j复制到两个新变量x,y中，以便之后向上下左右四个方向统计可以消灭的敌人数

    # 向上统计可以消灭的敌人数
    x = i
    y = j
    while (a[x][y] != '#'): #判断是不是墙，如果不是就继续
        # 如果当前点是敌人，则进行计数
        if (a[x][y] == 'G'):
            sum = sum + 1
        #     x--的作用是继续向上统计
        x = x - 1
    # 向下统计可以消灭的敌人数
    x = i
    y = j
    while (a[x][y] != '#'):
        # print (a[x][y])
        if (a[x][y] == 'G'):
            sum = sum + 1
        #     x++的作用是继续向下统计
        x = x + 1

    x = i
    y = j
    while (a[x][y] != '#'):
        if (a[x][y] == 'G'):
            sum = sum + 1
        y = y - 1

    x = i
    y = j
    while (a[x][y] != '#'):
        if (a[x][y] == 'G'):
            sum = sum + 1
        y = y + 1

    return sum


n = 13
m = 13

startx = 3
starty = 3
a = [['#' for col in range(n)] for row in range(m)]
book = [[0 for col in range(51)] for row in range(51)]

# init G
for i in [1, 2, 4, 5, 6, 8, 9, 10]:
    a[1][i] = 'G'
for i in [5, 7, 9, 11]:
    a[2][i] = 'G'
for i in [11]:
    a[3][i] = 'G'
for i in [1, 9, 11]:
    a[4][i] = 'G'
for i in [1, 2, 4, 5, 6, 10, 11]:
    a[5][i] = 'G'
for i in [1, 5]:
    a[6][i] = 'G'
for i in [2, 6]:
    a[7][i] = 'G'
for i in [1, 5, 11]:
    a[8][i] = 'G'
for i in [4, 6, 7, 8, 10, 11]:
    a[9][i] = 'G'
for i in [1, 5, 7, 11]:
    a[10][i] = 'G'
for i in [1, 2, 4, 5, 6, 8, 10, 11]:
    a[11][i] = 'G'

# init .
for i in [3, 11]:
    a[1][i] = '.'
for i in [3]:
    a[2][i] = '.'
for i in [1, 2, 3, 4, 5, 6, 7, 9, 10]:
    a[3][i] = '.'
for i in [3, 7]:
    a[4][i] = '.'
for i in [3, 7, 9]:
    a[5][i] = '.'
for i in [3, 7, 9]:
    a[6][i] = '.'
for i in [3, 4, 5, 7, 8, 9, 10, 11]:
    a[7][i] = '.'
for i in [3, 9]:
    a[8][i] = '.'
for i in [1, 2, 3, 9]:
    a[9][i] = '.'
for i in [3, 9]:
    a[10][i] = '.'
for i in [3, 9]:
    a[11][i] = '.'

next = numpy.array([[0, 1],  #向右走
                    [1, 0],  #向下走
                    [0, -1], #向左走
                    [-1, 0]]) #向上走

que = {}
for i in range(402):
    que[i] = Node(0,0)

head = 1
tail = 1
que[tail] = Node(startx, starty)
tail = tail + 1
book[startx][starty] = 1
max = getnum(startx, starty)

mx = startx
my = starty

while head < tail:
    for k in range(4):
        #尝试走的下一个点的坐标
        tx = que[head].x + next[k][0]
        ty = que[head].y + next[k][1]

        # 判断是否越界
        if tx < 0 or tx > n - 1 or ty < 0 or ty > m - 1:
            continue
        #判断是否为平地或者曾经走过
        if a[tx][ty] == '.' and book[tx][ty] == 0:
            # 每个点只入队一次，所以需要标记这个点已经走过
            book[tx][ty] = 1
            # 插入新扩展的点到队列中
            que[tail] =Node(tx, ty)
            tail = tail + 1
            # 统计当前新扩展的点可以消灭的敌人总数
            sum = getnum(tx, ty)
            # 更新max的值
            if sum > max:
                max = sum
                mx = tx
                my = ty
    head = head + 1

print("将炸弹放置在(%d, %d),最多可以消灭%d个敌人" % (mx, my, max))
