#!/usr/bin/python

# 图的遍历，深度优先

e = [[99999999 for col in range(101)] for row in range(101)]

e[1][2] = 2
e[1][5] = 10
e[2][3] = 3
e[2][5] = 7
e[3][1] = 4
e[3][4] = 4
e[4][5] = 5
e[5][3] = 3
e[1][1] = 0
e[2][2] = 0
e[3][3] = 0
e[4][4] = 0
e[5][5] = 0

n = 5
m = 8

book = [0 for col in range(101)]
min = 99999999


def dfs(cur, dis):
    global min, n
    if dis > min:
        return
    if cur == n:
        if dis < min:
            min = dis
        return

    for i in range(n):
        j = i + 1
        if e[cur][j] != 99999999 and book[j] == 0:
            book[j] = 1
            dfs(j, dis + e[cur][j])
            book[j] = 0
    return


book[1] = 1
dfs(1, 0)

print(min)
