#!/usr/bin/python

# 解救小哈

import numpy

m = 5
n = 4

a = [[0 for col in range(n)] for row in range(m)]

book = [[0 for col in range(n)] for row in range(m)]

a[0][2] = 1
a[2][2] = 1
a[3][1] = 1
a[4][3] = 1
startx = 0
starty = 0
p = 3
q = 2
min = 999999999;

def dfs(x, y, step):
    global p, q ,min, a , book
    next = numpy.array([[0, 1],[1, 0],[0,-1],[-1,0]])
    if(x==p and y==q):
        if (step<min):
            min=step
        return

    for k in range(4):
        tx=x+next[k][0]
        ty=y+next[k][1]
        if(tx<0 or tx>=m or ty<0 or ty>=n):
            continue
        if(a[tx][ty]==0 and book[tx][ty]==0):
            book[tx][ty]=1
            dfs(tx, ty, step+1)
            book[tx][ty]=0

    return

dfs(startx,starty,0)

print("{0}".format(min))