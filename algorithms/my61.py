#!/usr/bin/python

# Floyd-Warshall

inf = 99999999

e = [[inf for col in range(10)] for row in range(10)]

n = 4
m = 8

e[1][1] = 0
e[2][2] = 0
e[3][3] = 0
e[4][4] = 0


e[1][2]=2
e[1][3]=6
e[1][4]=4
e[2][3]=3
e[3][1]=7
e[3][4]=1
e[4][1]=5
e[4][3]=12

# Floyd-Warshall 算法核心语句

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if e[i][j]>e[i][k]+e[k][j]:
                e[i][j]=e[i][k]+e[k][j]



for i in range(1,n+1):
        print( *e[i][1:5])
