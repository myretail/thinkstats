#!/usr/bin/python

# Bellman-Ford

inf = 99999999

n = 5
m = 5

u = {}
v = {}
w = {}
dis = {}
bak = {}

u[1] = 2
v[1] = 3
w[1] = 2

u[2] = 1
v[2] = 2
w[2] = -3

u[3] = 1
v[3] = 5
w[3] = 5

u[4] = 4
v[4] = 5
w[4] = 2

u[5] = 3
v[5] = 4
w[5] = 3

for i in range(1, n + 1):
    dis[i] = inf

dis[1] = 0

for k in range(1, n):
    for i in range(1, n + 1):
        bak[i] = dis[i]

    for i in range(1, m + 1):
        if dis[v[i]] > dis[u[i]] + w[i]:
            dis[v[i]] = dis[u[i]] + w[i]

    check = 0

    for i in range(1, n + 1):
        if bak[i] != dis[i]:
            check = 1
            break
    if check == 0:
        break

flag = 0

for i in range(1, m + 1):
    if dis[v[i]] > dis[u[i]] + w[i]:
        flag = 1

if flag == 1:
    print("此图含有负权回路")
else:
    for i in range(1, n + 1):
        print(dis[i])
