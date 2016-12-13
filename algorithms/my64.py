#!/usr/bin/python

# Bellman-Ford 优化
from collections import deque

inf = 99999999

n = 5
m = 7

u = {}
v = {}
w = {}
dis = {}
book = {}
first = {}
next = {}
que = deque([])

u[1] = 1
v[1] = 2
w[1] = 2

u[2] = 1
v[2] = 5
w[2] = 10

u[3] = 2
v[3] = 3
w[3] = 3

u[4] = 2
v[4] = 5
w[4] = 7

u[5] = 3
v[5] = 4
w[5] = 4

u[6] = 4
v[6] = 5
w[6] = 5

u[7] = 5
v[7] = 3
w[7] = 6

for i in range(1, n + 1):
    dis[i] = inf
    book[i] = 0
    first[i] = -1

dis[1] = 0

for i in range(1, m + 1):
    next[i] = first[u[i]]
    first[u[i]] = i

que.append(1)
book[1] = 1

while len(que) > 0:
    head = que.popleft()
    k = first[head]
    while k != -1:
        if dis[v[k]] > dis[u[k]] + w[k]:
            dis[v[k]] = dis[u[k]] + w[k]
            if book[v[k]] == 0:
                que.append(v[k])
                book[v[k]] = 1
        k = next[k]

    book[head] = 0
    # temp= que.popleft()

for i in range(1, n + 1):
    print(dis[i])
