#!/usr/bin/python

#

class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w


n = 6
m = 9

e = [Edge(0, 0, 0), Edge(2, 4, 11), Edge(3, 5, 13), Edge(4, 6, 3), Edge(5, 6, 4), Edge(2, 3, 6), Edge(4, 5, 7),
     Edge(1, 2, 1), Edge(3, 4, 9), Edge(1, 3, 2)]

f = {}

sum = 0

count = 0


def quicksort(left, right):
    global e
    if left > right:
        return

    i = left
    j = right

    while i != j:
        while e[j].w >= e[left].w and i < j:
            j = j - 1

        while e[i].w <= e[left].w and i < j:
            i = i + 1

        if i < j:
            e[i], e[j] = e[j], e[i]

    e[left], e[i] = e[i], e[left]

    quicksort(left, i - 1)

    quicksort(i + 1, right)

    return


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
        return 1

    return 0


quicksort(1, m)

for i in range(1, n + 1):
    f[i] = i

for i in range(1, m + 1):
    if merge(e[i].u, e[i].v):
        count = count + 1
        sum = sum + e[i].w

    if count == n - 1:
        break

print(sum)
