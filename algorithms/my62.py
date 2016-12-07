#!/usr/bin/python

# Dijkstra

inf = 99999999

e = [[inf for col in range(10)] for row in range(10)]

n = 6
m = 9

e[1][1] = 0
e[2][2] = 0
e[3][3] = 0
e[4][4] = 0
e[5][5] = 0
e[6][6] = 0


e[1][2]=1
e[1][3]=12
e[2][3]=9
e[2][4]=3
e[3][5]=5
e[4][3]=4
e[4][5]=13
e[4][6]=15
e[5][6]=4


dis={}

for i in range(1, n+1):
    dis[i] = e[1][i]

book={}
for i in range(1,n+1):
    book[i]=0

book[1]=1

# Dijkstra 算法核心语句

for i in range(1, n):
    min =inf
    for j in range(1, n+1):
        if book[j]==0 and dis[j]<min:
            min=dis[j]
            u=j

    book[u]=1

    for v in range(1, n+1):
        if e[u][v]<inf:
            if dis[v]>dis[u]+e[u][v]:
                dis[v]=dis[u]+e[u][v]




for i in range(1,n+1):
    print(dis[i])


# first ={}
#
# for i in range(1, n+1):
#     first[i]=-1



