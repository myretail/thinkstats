#!/usr/bin/python


class Node:
    def __init__(self, x, y):
        self.x = x  # 横坐标
        self.y = y  # 纵坐标

    def __str__(self):
        return "({0},{1})".format(self.x,self.y)


a = [
    [0, 0, 0, 0, 0],
    [0, 5, 3, 5, 3],
    [0, 1, 5, 3, 0],
    [0, 2, 3, 5, 1],
    [0, 6, 1, 1, 5],
    [0, 1, 5, 5, 4]
]

n = 5
m = 4

book = [[0 for col in range(51)] for row in range(51)]

flag = 0

s=[]

def dfs(x, y, front):
    global flag
    if x == n and y == m + 1:
        flag = 1
        print(*s,sep='\n')
        return
    if x < 1 or x > n or y < 1 or y > m:
        return;

    if book[x][y] == 1:
        return

    book[x][y] = 1

    s.append(Node(x,y))

    if a[x][y] >= 5 and a[x][y] <= 6:
        if front == 1:
            dfs(x, y + 1, 1)
        if front == 2:
            dfs(x + 1, y, 2)
        if front == 3:
            dfs(x, y - 1, 3)
        if front == 4:
            dfs(x - 1, y, 4)

            #     当前水管是弯管的情况

    if a[x][y] >= 1 and a[x][y] <= 4:
        if front == 1:
            dfs(x + 1, y, 2)  # 3号状态
            dfs(x - 1, y, 4)  # 4号状态

        if front == 2:
            dfs(x, y + 1, 1)  # 一号状态
            dfs(x, y - 1, 3)  # 4号状态

        if front == 3:
            dfs(x - 1, y, 4)
            dfs(x + 1, y, 2)

        if front == 4:
            dfs(x, y + 1, 1)
            dfs(x, y - 1, 3)

    book[x][y] = 0
    s.pop()
    return


dfs(1, 1, 1)

if flag == 0:
    print("impossible")

