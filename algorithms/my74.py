#!/usr/bin/python

#
import numpy

f = {}

n = 10
m = 9


def init():
    global f, n
    for i in range(1, n + 1):
        f[i] = i


def getf(v):
    global f
    if f[v] == v:
        return v
    else:
        f[v] = getf(f[v])
        return f[v]


def merge(v, u):
    global f

    t1 = getf(v)
    t2 = getf(u)

    if t1 != t2:
        f[t2] = t1


init()

data = numpy.array([[1, 2],
                    [3, 4],
                    [5, 2],
                    [4, 6],
                    [2, 6],
                    [8, 7],
                    [9, 7],
                    [1, 6],
                    [2, 4]

                    ])

for i in range(m):
    merge(data[i][0], data[i][1])

sum = 0

for i in range(1, n + 1):
    if f[i] == i:
        sum += 1

print(sum)
